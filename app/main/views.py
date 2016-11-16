from flask import redirect, render_template, render_template_string, Blueprint,request,url_for
from flask_user import login_required,current_user
from . import main
from .forms import UserProfileForm,RoleForm
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


@main.route('/user/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    # Initialize form
    form = UserProfileForm(request.form, current_user)

    # Process valid POST
    if request.method == 'POST' and form.validate():
        # Copy form fields to user_profile fields
        form.populate_obj(current_user)

        # Save user_profile
        db.session.commit()

        # Redirect to home page
        return redirect(url_for('main.home_page'))

    # Process GET or invalid POST
    return render_template('main/user_profile_page.html',
                           form=form)