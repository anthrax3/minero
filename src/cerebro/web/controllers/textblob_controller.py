from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging
from cerebro.web.server import app
from cerebro.components import TextBlob

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
   document = request.args.get('document') if 'document' in request.args else ''
   result = textblob.nlp(document=document)
   return jsonify(result)

@app.route('/textblob/spelling_correction')
def textblob_spelling_correction():
   return render_template('textblob/spelling_correction.html',title='TextBlob')

@app.route('/api/textblob/spelling_correction', methods=['GET', 'POST'])
def api_textblob_spelling_correction():
   document = request.args.get('document') if 'document' in request.args else ''
   result = textblob.spelling_correction(document=document)
   return jsonify(result)

@app.route('/textblob/translation')
def textblob_translation():
   return render_template('textblob/translation.html',title='TextBlob')

@app.route('/api/textblob/translation', methods=['GET', 'POST'])
def api_textblob_translation():
   document = request.args.get('document') if 'document' in request.args else ''
   language = request.args.get('language') if 'language' in request.args else ''
   result = textblob.translate(document=document,language=language)
   return jsonify(result)

@app.route('/textblob/language_detection')
def textblob_language_detection():
   return render_template('textblob/language_detection.html',title='TextBlob')

@app.route('/api/textblob/language_detection', methods=['GET', 'POST'])
def api_textblob_language_detection():
   document = request.args.get('document') if 'document' in request.args else ''
   result = textblob.detect_language(document=document)
   return jsonify(result)



