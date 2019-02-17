"""
The flask application package.
"""

from os import environ
import os
import sys
import traceback
#import logging
from flask import Flask

app = Flask(__name__)
import web.controllers

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


