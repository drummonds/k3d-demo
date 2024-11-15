import os
import sys


from flask import Flask

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from . import settings

# create app
app = Flask(__name__, template_folder="web/templates", static_folder="web/static")
app.config.from_object("app.settings")

# register blueprints
from .web import bp as web

app.register_blueprint(web)
