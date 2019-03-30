from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging
from nlp.web.server import app
from nlp.components import TextBlob
from nlp.web.services import RequestService

logger = logging.getLogger(__name__)
textblob = TextBlob()

@app.route('/textblob')
def textblob_index():
   return render_template('textblob/index.html',title='TextBlob')

@app.route('/textblob/nlp')
def textblob_nlp():
   return render_template('textblob/nlp.html',title='TextBlob')

@app.route('/api/textblob/nlp', methods=['GET', 'POST'])
def api_textblob_nlp():
   document = RequestService().get_parameter('document')
   result = textblob.nlp(document=document)
   return jsonify(result)

@app.route('/textblob/spelling_correction')
def textblob_spelling_correction():
   return render_template('textblob/spelling_correction.html',title='TextBlob')

@app.route('/api/textblob/spelling_correction', methods=['GET', 'POST'])
def api_textblob_spelling_correction():
   document = RequestService().get_parameter('document')
   result = textblob.spelling_correction(document=document)
   return jsonify(result)

@app.route('/textblob/translation')
def textblob_translation():
   return render_template('textblob/translation.html',title='TextBlob')

@app.route('/api/textblob/translation', methods=['GET', 'POST'])
def api_textblob_translation():
   document = RequestService().get_parameter('document')
   language = RequestService().get_parameter('language')
   result = textblob.translate(document=document,language=language)
   return jsonify(result)

@app.route('/textblob/language_detection')
def textblob_language_detection():
   return render_template('textblob/language_detection.html',title='TextBlob')

@app.route('/api/textblob/language_detection', methods=['GET', 'POST'])
def api_textblob_language_detection():
   document = RequestService().get_parameter('document')
   result = textblob.detect_language(document=document)
   return jsonify(result)

@app.route('/api/textblob/models/download/<name>')
def api_textblob_models_download(name):
    textblob.models.download(name)
    return jsonify(textblob.models.get_status())

@app.route('/api/textblob/models/load/<name>')
def api_textblob_models_load(name):
    textblob.models.load(name)
    return jsonify(textblob.models.get_status())

@app.route('/api/textblob/models/unload/<name>')
def api_textblob_models_unload(name):
    textblob.models.unload(name)
    return jsonify(textblob.models.get_status())

@app.route('/api/textblob/models/status')
def api_textblob_models_status():
    return jsonify(textblob.models.get_status())


    
