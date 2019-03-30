import json
import os
import traceback
import sys
import datetime
import logging
from flask import render_template, redirect, request, jsonify

logger = logging.getLogger(__name__)

class RequestService(object):
   
   def __init__(self):
       pass

   def get_parameter(self, name):
        if request.args and name in request.args:
            return request.args.get(name)
        if request.json and name in request.json:
            return request.json.get(name)
        return ''