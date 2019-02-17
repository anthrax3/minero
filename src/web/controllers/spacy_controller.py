from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
import os
import traceback
import sys
import datetime
from web.server import app

@app.route('/spacy')
def dialogs_list():
    return render_template(
        'spacy/index.html',
        title='Spacy',
    )