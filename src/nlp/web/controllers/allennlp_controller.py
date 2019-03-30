from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging;
from nlp.web.server import app
from nlp.components import AllenNlp
from nlp.web.services import RequestService

logger = logging.getLogger(__name__)
allenNlp = AllenNlp()

@app.route('/allennlp')
def allennlp_index():
   return render_template('allennlp/index.html',title='AllenNlp')


@app.route('/allennlp/named_entity_recognition')
def allennlp_named_entity_recognition():
   return render_template('allennlp/named_entity_recognition.html',title='AllenNlp')

@app.route('/api/allennlp/named_entity_recognition', methods=['GET', 'POST'])
def api_allennlp_named_entity_recognition():
   document = RequestService().get_parameter('document')
   model = allenNlp.named_entity_recognition(document=document)
   return jsonify(model)

@app.route('/allennlp/constituency_parsing')
def allennlp_constituency_parsing():
   return render_template('allennlp/constituency_parsing.html',title='AllenNlp')

@app.route('/api/allennlp/constituency_parsing', methods=['GET', 'POST'])
def api_allennlp_constituency_parsing():
   document = RequestService().get_parameter('document')
   model = allenNlp.constituency_parsing(document=document)
   return jsonify(model)

@app.route('/allennlp/semantic_role_labeling')
def allennlp_semantic_role_labeling():
   return render_template('allennlp/semantic_role_labeling.html',title='AllenNlp')

@app.route('/api/allennlp/semantic_role_labeling', methods=['GET', 'POST'])
def api_allennlp_semantic_role_labeling():
   document = RequestService().get_parameter('document')
   model = allenNlp.semantic_role_labeling(document=document)
   return jsonify(model)

@app.route('/allennlp/machine_comprehension')
def allennlp_machine_comprehension():
   return render_template('allennlp/machine_comprehension.html',title='AllenNlp')

@app.route('/api/allennlp/machine_comprehension', methods=['GET', 'POST'])
def api_allennlp_machine_comprehension():
   document = RequestService().get_parameter('document')
   question = RequestService().get_parameter('question')
   model = allenNlp.machine_comprehension(document=document, question=question)
   return jsonify(model)

@app.route('/allennlp/textual_entailment')
def allennlp_textual_entailment():
   return render_template('allennlp/textual_entailment.html',title='AllenNlp')

@app.route('/api/allennlp/textual_entailment', methods=['GET', 'POST'])
def api_allennlp_textual_entailment():
   document = RequestService().get_parameter('document')
   hypothesis = RequestService().get_parameter('hypothesis')
   model = allenNlp.textual_entailment(document=document, hypothesis=hypothesis)
   return jsonify(model)

@app.route('/allennlp/coreference_resolution')
def allennlp_coreference_resolution():
   return render_template('allennlp/coreference_resolution.html',title='AllenNlp')

@app.route('/api/allennlp/coreference_resolution', methods=['GET', 'POST'])
def api_allennlp_coreference_resolution():
   document = RequestService().get_parameter('document')
   model = allenNlp.coreference_resolution(document=document)
   return jsonify(model)

@app.route('/allennlp/dependency_parsing')
def allennlp_dependency_parsing():
   return render_template('allennlp/dependency_parsing.html',title='AllenNlp')

@app.route('/api/allennlp/dependency_parsing', methods=['GET', 'POST'])
def api_allennlp_dependency_parsing():
   document = RequestService().get_parameter('document')
   model = allenNlp.dependency_parsing(document=document)
   return jsonify(model)


@app.route('/allennlp/open_information_extraction')
def allennlp_open_information_extraction():
   return render_template('allennlp/open_information_extraction.html',title='AllenNlp')

@app.route('/api/allennlp/open_information_extraction', methods=['GET', 'POST'])
def api_allennlp_open_information_extraction():
   document = RequestService().get_parameter('document')
   model = allenNlp.open_information_extraction(document=document)
   return jsonify(model)


@app.route('/allennlp/event2mind')
def allennlp_event2mind():
   return render_template('allennlp/event2mind.html',title='AllenNlp')

@app.route('/api/allennlp/event2mind', methods=['GET', 'POST'])
def api_allennlp_event2mind():
   document = RequestService().get_parameter('document')
   model = allenNlp.event2mind(document=document)
   return jsonify(model)

@app.route('/api/allennlp/models/download/<name>')
def api_allennlp_models_download(name):
        allenNlp.models.download(name)
        return jsonify(allenNlp.models.get_status())

@app.route('/api/allennlp/models/load/<name>')
def api_allennlp_models_load(name):
        allenNlp.models.load(name)
        return jsonify(allenNlp.models.get_status())

@app.route('/api/allennlp/models/unload/<name>')
def api_allennlp_models_unload(name):
        allenNlp.models.unload(name)
        return jsonify(allenNlp.models.get_status())

@app.route('/api/allennlp/models/status')
def api_allennlp_models_status():
        return jsonify(allenNlp.models.get_status())

@app.route('/api/allennlp/models/status/<name>')
def api_allennlp_models_status_by_name(name):
        return jsonify([allenNlp.models.get_status_by_name(name)])
