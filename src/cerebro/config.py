from os import environ
import os
import sys
import traceback
#import logging
from flask import Flask

path = os.path.dirname(os.path.abspath(__file__))
models_path = os.path.join(path, 'models')