"""
The flask application package.
"""

from os import environ
import os
import sys
import traceback
import logging
from flask import Flask
from flask import render_template, redirect, request, jsonify
from werkzeug.exceptions import HTTPException

logger = logging.getLogger(__name__)

app = Flask(__name__)
import miner.web.controllers

@app.errorhandler(Exception)
def handle_error(e):
    exception = "\n".join(traceback.format_exception(*sys.exc_info()))
    logger.error(exception)
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify({"error": str(e), "exception": exception}), code

class Server:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    host = environ.get('SERVER_HOST', '0.0.0.0')
    port = 5505

    try:
        port = int(environ.get('SERVER_PORT', '5505'))
    except ValueError:
        port = 5505

    def __init__(self):
        pass

    def run(self):
        app.run(self.host, self.port)
        pass


