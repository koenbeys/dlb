from flask import redirect, render_template, render_template_string, Blueprint,request,url_for
from flask_user import login_required,current_user
from . import main
# from .forms import UserProfileForm,RoleForm
from app import db

# The Home page is accessible to anyone
@main.route('/')
def home_page():
    return render_template('main/home_page.html')

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('common/404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('common/500.html'), 500

@main.route('/user')
@login_required  # Limits access to authenticated users
def user_page():
    print current_user.is_authenticated
    return render_template('main/user_page.html')

@main.route('/Role')
@login_required  # Limits access to authenticated users
def role_page():
    # Initialize form
    form = RoleForm(request.form)
    return render_template('main/role_page.html',
                           form=form)

@main.route('/info')
def info_page():
    print "info page"
    print render_template('main/info.html')
    return render_template('main/info.html')