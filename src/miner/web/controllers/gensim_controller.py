from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
import logging
from miner.web.server import app
from miner.components import Gensim
from miner.web.services import RequestService

logger = logging.getLogger(__name__)
gensim = Gensim()

@app.route('/gensim')
def gensim_index():
   return render_template('gensim/index.html',title='Gensim')

@app.route('/gensim/summarization')
def gensim_summarization():
   return render_template('gensim/summarization.html',title='Gensim')

@app.route('/api/gensim/summarization', methods=['GET', 'POST'])
def api_gensim_summarization():
   document = RequestService().get_parameter('document')
   try:
      ratio = float(request.args.get('ratio') if 'ratio' in request.args else '')
   except ValueError:
      ratio = 0.2
   try:
      word_count = int(request.args.get('word_count') if 'word_count' in request.args else '')
   except ValueError:
      word_count = None
   try:
      split = bool(request.args.get('split') if 'split' in request.args else 'True')
   except ValueError:
      split = True
   result = gensim.summarize(document=document, ratio=ratio, word_count=word_count, split=split)
   return jsonify(result)
