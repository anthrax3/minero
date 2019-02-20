from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
from web.server import app
from components import AllenNlp

@app.route('/allennlp')
def allennlp_index():
   return render_template(
      'spacy/index.html',
      title='Spacy',
   )

@app.route('/api/allennlp/named_entity_recognition')
def api_allennlp_named_entity_recognition():
   sentence = request.args.get('sentence') if 'sentence' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().named_entity_recognition(sentence=sentence)
   return jsonify(model)

@app.route('/api/allennlp/constituency_parsing')
def api_allennlp_constituency_parsing():
   sentence = request.args.get('sentence') if 'sentence' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().constituency_parsing(sentence=sentence)
   return jsonify(model)

@app.route('/api/allennlp/semantic_role_labeling')
def api_allennlp_semantic_role_labeling():
   sentence = request.args.get('sentence') if 'sentence' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().semantic_role_labeling(sentence=sentence)
   return jsonify(model)

@app.route('/api/allennlp/machine_comprehension')
def api_allennlp_machine_comprehension():
   passage = request.args.get('passage') if 'passage' in request.args else ''
   question = request.args.get('question') if 'question' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().machine_comprehension(passage=passage, question=question)
   return jsonify(model)

@app.route('/api/allennlp/textual_entailment')
def api_allennlp_textual_entailment():
   hypothesis = request.args.get('hypothesis') if 'hypothesis' in request.args else ''
   premise = request.args.get('premise') if 'premise' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().textual_entailment(hypothesis=hypothesis, premise=premise)
   return jsonify(model)

@app.route('/api/allennlp/coreference_resolution')
def api_allennlp_coreference_resolution():
   document = request.args.get('document') if 'document' in request.args else ''
   #pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model = AllenNlp().coreference_resolution(document=document)
   return jsonify(model)
