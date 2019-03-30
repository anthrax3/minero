from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging
from nlp.web.server import app
from nlp.components import Nltk
from nlp.web.services import RequestService

logger = logging.getLogger(__name__)
nltk = Nltk()

@app.route('/nltk')
def nltk_index():
   return render_template('nltk/index.html',title='nltk')

@app.route('/nltk/vader_sentiment_analysis')
def nltk_vader_sentiment_analysis():
   return render_template('nltk/vader_sentiment_analysis.html',title='TextBlob')

@app.route('/api/nltk/vader_sentiment_analysis', methods=['GET', 'POST'])
def api_vader_sentiment_analysis_nlp():
   document = RequestService().get_parameter('document')
   result = nltk.vader_sentiment_analysis(document=document)
   return jsonify(result)

@app.route('/api/nltk/models/download/<name>')
def api_nltk_models_download(name):
    nltk.models.download(name)
    return jsonify(nltk.models.get_status())

@app.route('/api/nltk/models/load/<name>')
def api_nltk_models_load(name):
    nltk.models.load(name)
    return jsonify(nltk.models.get_status())

@app.route('/api/nltk/models/unload/<name>')
def api_nltk_models_unload(name):
    nltk.models.unload(name)
    return jsonify(nltk.models.get_status())

@app.route('/api/nltk/models/status')
def api_nltk_models_status():
    return jsonify(nltk.models.get_status())


