# This file starts the WSGI web application.
# - Heroku starts gunicorn, which loads Procfile, which starts manage.py

import os
from app import create_app
from app import user
from app import dlb
from flask import render_template
from lib import SetDebug,AdsVar

import logging
logger = logging.getLogger("app")

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
user.create_mod()
dlb.create_mod()


logger.info("init done ")
from app import manager

if __name__ == "__main__":
    manager.run()





