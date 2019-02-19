from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
from web.server import app
from components import Spacy

@app.route('/spacy')
def spacy_index():
   return render_template(
      'spacy/index.html',
      title='Spacy',
   )

@app.route('/api/spacy')
def api_spacy():
   text = request.args.get('text') if 'text' in request.args else ''
   pretty = request.args.get('pretty').lower() in ("yes", "true", "t", "1") if 'pretty' in request.args else False
   model_dict = Spacy().to_dict(text)
   return jsonify(model_dict)

@app.route('/api/spacy/similarity')
def api_spacy_similarity():
   text = request.args.get('text') if 'text' in request.args else ''
   text2 = request.args.get('text2') if 'text2' in request.args else ''
   text_spacy = Spacy().to_spacy(text)
   text2_spacy = Spacy().to_spacy(text2)
   return jsonify({"similarity": text_spacy.similarity(text2_spacy)})
    