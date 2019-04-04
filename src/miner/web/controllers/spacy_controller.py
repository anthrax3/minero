from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging;
from miner.web.server import app
from miner.components import Spacy
from miner.web.services import RequestService

logger = logging.getLogger(__name__)
spacy = Spacy()

@app.route('/spacy')
def spacy_index():
   return render_template('spacy/index.html',title='Spacy')

@app.route('/spacy/nlp')
def spacy_index_nlp():
   return render_template('spacy/miner.html',title='Spacy')

@app.route('/api/spacy/nlp')
def api_spacy():
        model = RequestService().get_parameter('model')
        document = RequestService().get_parameter('document')
        result = spacy.nlp(model, document)
        return jsonify(result)
   
@app.route('/spacy/similarity')
def spacy_index_similarity():
   return render_template('spacy/similarity.html',title='Spacy')

@app.route('/api/spacy/similarity')
def api_spacy_similarity():
   model = RequestService().get_parameter('model')
   document = RequestService().get_parameter('document')
   similarTo = RequestService().get_parameter('similarTo')
   result = spacy.similarity(model, document, similarTo)
   return jsonify(result)
    
@app.route('/api/spacy/models/download/<name>')
def api_spacy_models_download(name):
        spacy.models.download(name)
        return jsonify(spacy.models.get_status())

@app.route('/api/spacy/models/load/<name>')
def api_spacy_models_load(name):
        spacy.models.load(name)
        return jsonify(spacy.models.get_status())

@app.route('/api/spacy/models/unload/<name>')
def api_spacy_models_unload(name):
        spacy.models.unload(name)
        return jsonify(spacy.models.get_status())

@app.route('/api/spacy/models/status')
def api_spacy_models_status():
        return jsonify(spacy.models.get_status())

