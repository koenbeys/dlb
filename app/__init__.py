# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())


app = Flask(__name__)           # The WSGI compliant web application object
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)            # Setup Flask-SQLAlchemy
manager = Manager(app)          # Setup Flask-Script

from app.startup.create_app import create_app