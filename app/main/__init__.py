# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Blueprint

main = Blueprint('main', __name__)

from . import forms
from . import views
from . import models




