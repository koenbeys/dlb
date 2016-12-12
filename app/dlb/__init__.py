# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.
from flask import Blueprint

#dlb = Blueprint('dlb', __name__,template_folder='templates',static_folder='static')
dlb = Blueprint('dlb', __name__,template_folder='templates')
from . import forms
from . import views
from . import models
from . import functions



def create_mod():
# Setup dlb to handle user account related forms

    from app import app, db
    import os

    from app.dlb import dlb as dlb_blueprint
    app.register_blueprint(dlb_blueprint)

    # from app.usr import user as user_blueprint
    # app.register_blueprint(user_blueprint)

    #create app directories if not exist
    directory = app.config['DLB_UPLOAD_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = app.config['DLB_BACKUP_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = app.config['DLB_DOWNLOAD_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)

    directory = app.config['DLB_ZRX_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)