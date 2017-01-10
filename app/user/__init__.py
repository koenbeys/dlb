# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Blueprint
from flask_user import UserManager, SQLAlchemyAdapter
import logging

#
# blueprint , logging , declaratie => moet voor  import van models staan
#

user = Blueprint('user', __name__,template_folder='templates')

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
from . import models
from . import views



def create_mod():

    log.debug('start procedure')

    from .models import User
    from .forms import MyRegisterForm
    from .views import user_profile_page
    from app import app, db

    log.debug('start procedure')

    # Blueprint registratie user_blueprint

    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    log.debug('register_blueprint user_blueprint')

    # Setup Flask-User to handle user account related forms

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    user_manager = UserManager(db_adapter, app,  # Init Flask-User and bind to app
                               register_form=MyRegisterForm,  # using a custom register form with UserProfile fields
                               user_profile_view_function=user_profile_page,
                           )
    log.debug('Setup Flask-User to handle user account related forms')
    log.debug('end procedure')
