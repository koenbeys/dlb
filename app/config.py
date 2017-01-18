import os
basedir = os.path.abspath(os.path.dirname(__file__))
import logging
import logging.handlers

class Config:

    # ***********************************
    # Settings common to all environments
    # ***********************************

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string expl '
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Application settings
    APP_NAME = "Enki App"
    APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

#   logging

    # LOG_FOLDER='logs2'
    LOG_LEVEL = logging.DEBUG
    LOG_FORMATTER   = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    # LOG_DEBUG_FORMATTER=logging.Formatter('%(asctime)s - %(levelno)s - %(name)s,%(module)s,%(lineno)d  - %(message)s')


    # Flask settings
    CSRF_ENABLED = True
    FLASK_SERVER_HOST = "127.0.0.1"
    FLASK_SERVER_PORT=5106
#    FLASK_SERVER_HOST = "0.0.0.0"
#    FLASK_SERVER_PORT=80

    # Mail settings
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = '"'+ APP_NAME + '" <noreply@example.com>'
    MAIL_SERVER = 'smtp.vlaanderen.be'
    MAIL_PORT = 25

    # Flask-User settings
    USER_APP_NAME = APP_NAME
    USER_ENABLE_CHANGE_PASSWORD = True  # Allow users to change their password
    USER_ENABLE_CHANGE_USERNAME = False  # Allow users to change their username
    USER_ENABLE_CONFIRM_EMAIL = True  # Force users to confirm their email
    USER_ENABLE_FORGOT_PASSWORD = True  # Allow users to reset their passwords
    USER_ENABLE_EMAIL = True  # Register with Email
    USER_ENABLE_REGISTRATION = False  # Allow new users to register
    USER_ENABLE_RETYPE_PASSWORD = True  # Prompt for `retype password` in:
    USER_ENABLE_USERNAME = True  # Register and Login with username
    USER_AFTER_LOGIN_ENDPOINT = 'main.home_page'
    USER_AFTER_LOGOUT_ENDPOINT = 'main.home_page'

    DLB_UPLOAD_FOLDER = 'uploads/'
    DLB_DOWNLOAD_FOLDER = 'downloads/'
    DLB_BACKUP_FOLDER = 'backup/'

    DLB_ZRX_FOLDER = 'zrx_files/'
    DLB_ZRX_FILE_EXTENSION = 'zrx'
    DLB_GAUGE_TO_ZRX = True
    DLB_SENSOR_TO_ZRX = False
    DLB_STATIONLIST_FILENAME = "stations.txt"

    DLB_NB_STATION_HISTORY_ITEMS = 5
    DLB_NB_HISTO_HISTORY_ITEMS = 10

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
