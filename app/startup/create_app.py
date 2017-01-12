import os
import os.path

from app.config import config

from flask_migrate import Migrate, MigrateCommand
from flask_wtf.csrf import CsrfProtect
from flask_mail import Mail
from flask_script import Shell, Server
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from app import app, db, manager
import logging.handlers
import logging


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

    from flask_login import current_user

    class AddUsername2Log(logging.Filter):
        def filter(self, record):
            # from flask_login import current_user
            try:
                record.username = current_user.username
            except:
                record.username = "na"
            #
            return True

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
    #
    # # Setup Flask-User to handle user account related forms
    # from app.main.models import User
    # from app.main.forms import MyRegisterForm
    # from app.main.views import user_profile_page
    #
    # db_adapter = SQLAlchemyAdapter(db, User)  # Setup the SQLAlchemy DB Adapter
    # user_manager = UserManager(db_adapter, app,  # Init Flask-User and bind to app
    #                            register_form=MyRegisterForm,  # using a custom register form with UserProfile fields
    #                            user_profile_view_function=user_profile_page,
    # )

    # Setup WTForms CsrfProtect
    CsrfProtect(app)

    # Load all blueprints with their manager commands, models and views

    from app.main import main
    app.register_blueprint(main)

    #
    # Creatie Log Folder
    #

    if 'LOG_FOLDER' not in app.config:
        app.config['LOG_FOLDER'] = os.path.join(os.getcwd(),"log")

    directory = app.config['LOG_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
    app.config['LOG_FOLDER'] =os.path.abspath(directory)

    #
    # Creatie Log Folder, Default is debug folder = log folder
    #

    if 'LOG_DEBUG_FOLDER' not in app.config:
        app.config['LOG_DEBUG_FOLDER'] = app.config['LOG_FOLDER']

    directory = app.config['LOG_DEBUG_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
    app.config['LOG_DEBUG_FOLDER'] =os.path.abspath(directory)

    #
    #   init logger & default settings
    #
    log = logging.getLogger('app')

    if 'LOG_LEVEL' not in app.config:
        app.config['LOG_LEVEL']=logging.DEBUG

    log.setLevel(app.config['LOG_LEVEL'])


    if 'LOG_FORMATTER' not in app.config:
        app.config['LOG_FORMATTER']=logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    if 'LOG_ERROR_FORMATTER' not in app.config:
        app.config['LOG_ERROR_FORMATTER']=app.config['LOG_FORMATTER']
    if 'LOG_INFO_FORMATTER' not in app.config:
        app.config['LOG_INFO_FORMATTER']=app.config['LOG_FORMATTER']
    if 'LOG_DEBUG_FORMATTER' not in app.config:
        app.config['LOG_DEBUG_FORMATTER']=logging.Formatter('%(asctime)s - %(levelno)s - %(username)s:%(thread)d - %(name)s,%(module)s,%(lineno)d  - %(message)s')

    #
    #   init Error logger
    #

    if 'LOG_ERROR_FILENAME' not in app.config:
        app.config['LOG_ERROR_FILENAME']='error.log'

    fh_error = logging.FileHandler(os.path.join(app.config['LOG_FOLDER'],app.config['LOG_ERROR_FILENAME']))
    fh_error.setFormatter(app.config['LOG_ERROR_FORMATTER'])
    fh_error.setLevel(logging.ERROR)
    log.addHandler(fh_error)
    log.info("error logging set")

    #
    #   init INFO logger
    #

    if 'LOG_INFO_FILENAME' not in app.config:
        app.config['LOG_INFO_FILENAME']='info.log'

    fh_info = logging.FileHandler(os.path.join(app.config['LOG_FOLDER'],app.config['LOG_INFO_FILENAME']))
    fh_info.setFormatter(app.config['LOG_INFO_FORMATTER'])
    fh_info.setLevel(logging.INFO)
    log.addHandler(fh_info)
    log.info("info logging set")

    #
    #   init INFO logger
    #

    if 'LOG_DEBUG_FILENAME' not in app.config:
        app.config['LOG_DEBUG_FILENAME']='debug.log'

    fh_debug = logging.FileHandler(os.path.join(app.config['LOG_DEBUG_FOLDER'],app.config['LOG_DEBUG_FILENAME']))
    fh_debug.addFilter(AddUsername2Log())
    fh_debug.setFormatter(app.config['LOG_DEBUG_FORMATTER'])
    fh_debug.setLevel(logging.DEBUG)
    log.addHandler(fh_debug)
    log.info("debug logging set")

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app