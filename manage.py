# This file starts the WSGI web application.
# - Heroku starts gunicorn, which loads Procfile, which starts manage.py

import os
from app import create_app
from flask import render_template

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#
# @app.route('/')
# def hello_world():
# #    return 'Hello, World!'
#     return render_template('main/home_page.html',AppName="koen")

# Start a development web server if executed from the command line
if __name__ == "__main__":
    # Manage the command line parameters such as:
    # - python manage.py runserver
    # - python manage.py db
    from app import manager
#    app.run(port=5001,debug=True)
    manager.run()
