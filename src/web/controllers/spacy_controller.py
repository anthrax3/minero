from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging;
from web.server import app
from components import Spacy

logger = logging.getLogger(__name__)
spacy = Spacy()

@app.route('/spacy')
def spacy_index():
   return render_template(
      'spacy/index.html',
      title='Spacy',
   )

@app.route('/spacy/nlp')
def spacy_index_nlp():
   return render_template(
      'spacy/nlp.html',
      title='Spacy',
   )

@app.route('/api/spacy')
def api_spacy():
    try:
        text = request.args.get('text') if 'text' in request.args else ''
        model = request.args.get('model') if 'model' in request.args else ''
        pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
        model_dict = spacy.nlp(model, text)
        return jsonify(model_dict)
    except Exception as e:
        logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response
   

@app.route('/api/spacy/similarity')
def api_spacy_similarity():
   text = request.args.get('text') if 'text' in request.args else ''
   text2 = request.args.get('text2') if 'text2' in request.args else ''
   text_spacy = spacy.to_spacy(text)
   text2_spacy = spacy.to_spacy(text2)
   return jsonify({"similarity": text_spacy.similarity(text2_spacy)})
    
@app.route('/api/spacy/models/download/<name>')
def api_spacy_models_download(name):
    try:
        spacy.download_model(name)
        return jsonify(spacy.get_model_status())
    except Exception as e:
        logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response

@app.route('/api/spacy/models/load/<name>')
def api_spacy_models_load(name):
    try:
        spacy.load_model(name)
        return jsonify(spacy.get_model_status())
    except Exception as e:
        logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response

@app.route('/api/spacy/models/unload/<name>')
def api_spacy_models_unload(name):
    try:
        spacy.unload_model(name)
        return jsonify(spacy.get_model_status())
    except Exception as e:
        logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response

@app.route('/api/spacy/models/status')
def api_spacy_models_status():
    try:
        return jsonify(spacy.get_model_status())
    except Exception as e:
        logger.error("\n". join(traceback.format_exception(*sys.exc_info())))
        response = jsonify({"error": str(e)})
        response.status_code = 400
        return response
