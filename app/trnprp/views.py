from flask import redirect, render_template, render_template_string, Blueprint,request,url_for
from flask_user import login_required,current_user
from . import main

@main.route('/proj')
@login_required  # Limits access to authenticated users
def user_page():
    return render_template('proj/proj.html')
