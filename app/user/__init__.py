# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.
from flask import Blueprint

from flask_user import UserManager, SQLAlchemyAdapter

user = Blueprint('user', __name__,template_folder='templates')
from . import forms
from . import views
from . import models



def create_mod():
# Setup Flask-User to handle user account related forms
    from .models import User
    from .forms import MyRegisterForm
    from .views import user_profile_page
    from app import app, db

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    user_manager = UserManager(db_adapter, app,  # Init Flask-User and bind to app
                               register_form=MyRegisterForm,  # using a custom register form with UserProfile fields
                               user_profile_view_function=user_profile_page,
                           )


    from app.user import user as user_blueprint
    app.register_blueprint(user_blueprint)