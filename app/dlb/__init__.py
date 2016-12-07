# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.
from flask import Blueprint

dlb = Blueprint('dlb', __name__,template_folder='templates',static_folder='static')
#dlb = Blueprint('dlb', __name__,template_folder='templates')
from . import forms
from . import views
from . import models
from . import functions
