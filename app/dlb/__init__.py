# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Blueprint
import logging

#
# blueprint , logging , declaratie => moet voor  import van models staan
#

#dlb = Blueprint('dlb', __name__,template_folder='templates',static_folder='static')
dlb = Blueprint('dlb', __name__,template_folder='templates')

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


# imports

from . import forms
from . import views
from . import models
from . import functions
from . import classes

def create_mod():
    # from app import app
    # log.setLevel(app.config['LOG_LEVEL'])
    log.debug('start procedure create_mod')
    # Setup dlb to handle user account related forms

    from app import app, db
    import os

    # Blueprint registratie dlb_blueprint

    from app.dlb import dlb as dlb_blueprint
    app.register_blueprint(dlb_blueprint)

    log.debug('register_blueprint dlb_blueprint')

    #create app directories if not exist
    directory = app.config['DLB_UPLOAD_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info("Create directory %s",directory)

    directory = app.config['DLB_BACKUP_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info("Create directory %s",directory)

    directory = app.config['DLB_DOWNLOAD_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info("Create directory %s",directory)

    directory = app.config['DLB_ZRX_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
        log.info("Create directory %s",directory)

    log.debug('finish checking directory & creatie')
    log.debug('end procedure create_mod')