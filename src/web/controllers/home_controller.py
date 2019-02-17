from datetime import datetime
from flask import render_template, redirect, request, jsonify
import json
from web.server import app

@app.route('/')
def index():
    return render_template(
       'home/index.html',
        title='Home',
        year=datetime.now().year,
    )