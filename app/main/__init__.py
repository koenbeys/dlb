# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Blueprint
import logging

main = Blueprint('main', __name__)

#
#   initiate logger
#

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
logging.getLogger(__name__).addHandler(NullHandler())
log = logging.getLogger(__name__)

from . import forms
from . import views
from . import models




