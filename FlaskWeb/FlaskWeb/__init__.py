"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')
app.register_blueprint(bp)

import FlaskWeb.views
