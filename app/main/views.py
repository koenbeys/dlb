from flask import redirect, render_template, render_template_string, Blueprint,request,url_for,session
from flask_user import login_required,current_user
from . import main
from . import log
from .forms import RoleForm



# from .forms import UserProfileForm,RoleForm
from app import db

# The Home page is accessible to anyone
@main.route('/')
def home_page():
    # print current_user.__dict__
    log.debug("start def home_page")
    return render_template('home_page.html')

@main.app_errorhandler(404)
def page_not_found(e):
    from inspect import stack
    log.debug("start page_not_found %s from %s",stack()[0][3],stack()[1][3])
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    log.debug("start def internal_server_error")
    return render_template('500.html'), 500



