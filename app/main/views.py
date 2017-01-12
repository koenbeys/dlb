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
    log.debug("start def home_page")
    return render_template('main/home_page.html')

@main.app_errorhandler(404)
def page_not_found(e):
    from inspect import stack
    # print "-----------------> ", stack()[0][3], "  from   ", stack()[1][3]
    log.debug("start page_not_found %s from %s",stack()[0][3],stack()[1][3])
    return render_template('main/404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    log.debug("start def internal_server_error")
    return render_template('common/500.html'), 500

@main.route('/user')
@login_required  # Limits access to authenticated users
def user_page():
    log.debug("start def user_page")
    return render_template('main/user_page.html')

@main.route('/Role')
@login_required  # Limits access to authenticated users
def role_page():
    log.debug("start def role_page")
    # Initialize form
    form = RoleForm(request.form)
    return render_template('main/role_page.html',
                           form=form)

@main.route('/info')
def info_page():
    log.debug("start def info_page")
    return render_template('main/info.html')