Vue.prototype.$fetch = function (url = ``, parameters = {}) {
    return fetch(url, parameters)
        .then(r => r.text().then(text => ({ ok: r.ok, status: r.status, statusText: r.statusText, text: text })))
        .then(r => {
            if (r.text) {
                try {
                    r.json = JSON.parse(r.text) 
                } catch (e) {
                    console.log("Response from server the server: " + r.text)
                }
                return r;
            }
            return r;
         })
        .then(response => {
            if (response.json && response.json.error)
                throw Error(response.json.error);
            if (!response.ok)
                throw Error(response.status + ': ' + response.statusText);
            return response.json;
        })
};

Vue.component('text-editor', {
    props: ['value'],
    watch: {
        value: function (val, oldVal) {
            if (val != this.textEditor.getValue()) {
                this.textEditor.setValue(val ? val : '');
            }
        },
    },
    mounted: function () {
        var scope = this;
        this.textEditor = CodeMirror.fromTextArea(this.$refs.text_editor, {
            lineNumbers: false,
            lineWrapping: true
        });
        this.textEditor.on('change', function (cm) {
            scope.textEditor.save();
            scope.$emit('input', cm.getValue())
        });
        this.textEditor.setValue(this.value ? this.value : '');
        this.textEditor.setSize("100%", "100%");
    },
    template: '<textarea ref="text_editor"></textarea>'
});

Vue.component('json-viewer', {
    props: ['value'],
    watch: {
        value: function (val) {
            this.$refs.myPre.innerHTML = this.syntaxHighlight(this.stringify(val));
        },
    },

    methods: {
        syntaxHighlight: function (json) {
            json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
            return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
                var cls = 'number';
                if (/^"/.test(match)) {
                    if (/:$/.test(match)) {
                        cls = 'key';
                    } else {
                        cls = 'string';
                    }
                } else if (/true|false/.test(match)) {
                    cls = 'boolean';
                } else if (/null/.test(match)) {
                    cls = 'null';
                }
                return '<span class="' + cls + '">' + match + '</span>';
            });
        },
        stringify: function (json) {
            if (json)
                return JSON.stringify(json, undefined, 4);
            else
                return null;
        }
    },
    mounted: function () {
        var scope = this;
    },
    template: '<div><pre ref="myPre"></pre></div>'
});

Vue.component('models', {
    props: ['component', 'model'],
    data: function () {
        return {
            models: null,
            download_clicked: {},
            download_error: {},
            load_clicked: {},
            load_error: {},
            unload_clicked: {},
            unload_error: {},
        }
    },
    methods: {
        download: function (name) {
            if (this.download_clicked[name])
                return;
            this.download_clicked[name] = true;
            this.download_error[name] = null;
            this.$fetch(
                `/api/${this.component}/models/download/${encodeURIComponent(name)}`, {
                    method: "GET"
                })
                .then(json => {
                    this.models = json;
                    this.download_clicked[name] = false;
                })
                .catch(error => {
                    this.download_error[name] = "Error: " + error.message;
                    this.download_clicked[name] = false;
                });
        },
        load: function (name) {
            if (this.load_clicked[name])
                return;
            this.load_clicked[name] = true;
            this.load_error[name] = null;
            this.$fetch(
                `/api/${this.component}/models/load/${encodeURIComponent(name)}`, {method: "GET"})
                .then(json => {
                    this.models = json;
                    this.load_clicked[name] = false;
                })
                .catch(error => {
                    this.load_error[name] = "Error: " + error.message;
                    this.load_clicked[name] = false;
                });
        },
        unload: function (name) {
            if (this.unload_clicked[name])
                return;
            this.unload_clicked[name] = true;
            this.$fetch(
                    `/api/${this.component}/models/unload/${encodeURIComponent(name)}`, {method: "GET"})
                .then(json => {
                    this.models = json;
                    this.unload_clicked[name] = false;
                })
                .catch(error => {
                    this.unload_error[name] = "Error: " + error.message;
                    this.unload_clicked[name] = false;
                });
        },
        update_models_status: function () {
            var url = this.model ?
                `/api/${this.component}/models/status/${this.model}` :
                `/api/${this.component}/models/status`

            this.$fetch(url, { method: "GET" })
                .then(json => {
                    this.models = json;
                })
                .catch(error => {
                    this.error = "Error: " + error.message;
                });
        }
    },
    mounted: function () {
        this.timer = setInterval(this.update_models_status, 2000);
        
    },
    template: `
<ul style="padding-left: 20px">
    <li v-for="model in models">
        <a v-bind:href="model.url" class="text-dark">{{model.displayName || model.name}}</a> <span class="text-muted">{{model.size}}</span> 
        <div class="text-muted">{{model.description}}</div> 
        <div>
        <div class="d-inline-block align-top">
            <div v-if="model.is_downloaded && !model.is_loaded" class="mr-5">
                <button v-on:click.stop.prevent="load(model.name)" type="button" class="btn btn-sm btn-outline-secondary">
                    Load
                    <span v-if="load_clicked[model.name]" class="loader"></span>
                </button>
            <div v-if="load_error[model.name]">{{ load_error[model.name] }}</div>
        </div>
        <div v-if="model.is_loaded" class="mr-5">
            <button v-on:click.stop.prevent="unload(model.name)" type="button" class="btn btn-sm btn-outline-secondary">
                Unload
                <span v-if="unload_clicked[model.name]" class="loader"></span>
            </button>
            <div v-if="unload_error[model.name]">{{ load_error[model.name] }}</div>
        </div>
        </div>
            <div class="d-inline-block align-top">
                <button v-on:click.stop.prevent="download(model.name)" type="button" class="btn btn-sm btn-outline-secondary">
                    Download
                    <span v-if="download_clicked[model.name] || model.is_downloading" class="loader"></span>
                </button>
                <div v-if="download_error[model.name]">{{ download_error[model.name] }}</div>
                <div class="text-muted">{{ model.download_status }} <span v-if="model.download_percentage">{{ model.download_percentage }}%</span></div>
                <div>{{ model.download_error }}</div>
            </div>
        </div>
    </li>
</ul>`
});

