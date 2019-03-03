from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging
from web.server import app
from components import Gensim

logger = logging.getLogger(__name__)
gensim = Gensim()

@app.route('/gensim')
def gensim_index():
   return render_template(
      'gensim/index.html',
      title='Gensim',
   )

@app.route('/gensim/summarization')
def gensim_summarization():
   return render_template(
      'gensim/summarization.html',
      title='Gensim',
   )

@app.route('/api/gensim/summarization', methods=['GET', 'POST'])
def api_gensim_summarization():
   document = request.args.get('document') if 'document' in request.args else ''
   result = gensim.summarize(document=document)
   return jsonify(result)
