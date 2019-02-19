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
        value: function (val) {
            if (val != this.textEditor.getValue()) {
                this.textEditor.setValue(val ? val : '');
            }
        },
    },
    mounted: function () {
        var scope = this;
        this.textEditor = CodeMirror.fromTextArea(document.getElementById('text_editor'), {
            lineNumbers: false
        });
        this.textEditor.on('change', function (cm) {
            scope.textEditor.save();
            scope.$emit('input', cm.getValue())
            //var info = this.textEditor.getScrollInfo();
            //document.getElementsByClassName("CodeMirror")[0].style.minWidth = info.width + "px";
        });
        this.textEditor.setValue(this.value ? this.value : '');
        this.textEditor.setSize("100%", "100%");

        //var info = this.textEditor.getScrollInfo();
        //document.getElementsByClassName("CodeMirror")[0].style.minWidth = info.width + "px";
    },
    template: '<textarea id="text_editor"></textarea>'
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

