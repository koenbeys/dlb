import os

from app.config import config

from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail
from flask_script import Shell, Server
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from app import app, db, manager

from flask_user import UserManager, SQLAlchemyAdapter

# zorgt ervoor dat model beschikbaar is van proj
from app.dlb import models

def make_shell_context():
    return dict(app=app, db=db)


@app.before_first_request
def initialize_app_on_first_request():
    # print "---before_first_request-----------"
    db.create_all()
    from .create_users import create_users
    create_users()

def create_app(config_name):

    """
    Initialize Flask applicaton
    """

    # ***** Initialize app config settings *****
    # Read common settings from 'app/config.py' file

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    if app.testing:
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF checks while testing


    # Setup Flask-Migrate
    migrate = Migrate(app, db)
    manager.add_command('db', MigrateCommand)

    manager.add_command("runserver", Server(host=app.config['FLASK_SERVER_HOST'],port=app.config['FLASK_SERVER_PORT']))
    manager.add_command("shell", Shell(make_context=make_shell_context))


    # Setup Flask-Mail
    mail = Mail(app)

    # Setup Flask Bootstrap
    bootstrap = Bootstrap(app)

    # Setup Flask moment (tijd)
    moment = Moment(app)

    # Setup Flask-User to handle user account related forms
    from app.main.models import User
    from app.main.forms import MyRegisterForm
    from app.main.views import user_profile_page

    db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    user_manager = UserManager(db_adapter, app,  # Init Flask-User and bind to app
                               register_form=MyRegisterForm,  # using a custom register form with UserProfile fields
                               user_profile_view_function=user_profile_page,
    )

    # Setup WTForms CsrfProtect
    CsrfProtect(app)

    # Load all blueprints with their manager commands, models and views

    from app.main import main
    app.register_blueprint(main)

    from app.dlb import dlb as dlb_blueprint
    app.register_blueprint(dlb_blueprint)


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


    return app