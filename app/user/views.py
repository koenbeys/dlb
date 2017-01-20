from flask import redirect, render_template, request,url_for, flash
from flask_user import login_required,current_user
# from flask_login import login_user,abort
# from .functions import is_safe_url
from . import user,log
from .forms import userdetailForm,LoginForm,UserProfileForm, userListForm
from app import app,db
from . import functions
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)
#
#         flash('Logged in successfully.!!!')
#
#         next = request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return abort(400)
#
#         return redirect(next or url_for('index'))
#     return render_template('login.html', form=form)


@user.route('/userList', methods=['GET', 'POST'])
def userList_page():
    log.debug('start def userList_page')
    form = userListForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "Userlistform : ok"
            userid1 = request.form.get('userid')
            op = request.form.get('op')
            print userid1
            print op
            if (op == "new"):
                return redirect(url_for('user.newuser_page'))
            else:
                if (op == "edit"):
                    return redirect(url_for('user.userdetail_page', userid=userid1))
                else:
                    print "password update"
                    # should be page for password update

                    return redirect(url_for('user.change_password', userid=userid1))

                    # return redirect(url_for('user.set_password_page', userid=userid1))
        else:
            print "Userlistform : not ok"
            userList = functions.getUserList()
            return render_template( 'userlist.html', tableList=userList, alert=True)

    userList = functions.getUserList()
    return render_template('userList.html', tableList=userList, alert=False)

# @user.route('/set_password/<userid>', methods=['GET', 'POST'])
# def change_password():
#     """ Prompt for old password and new password and change the user's password."""
#     user_manager =  current_app.user_manager
#     db_adapter = user_manager.db_adapter
#
#     # Initialize form
#     form = user_manager.change_password_form(request.form)
#     form.next.data = request.args.get('next', _endpoint_url(user_manager.after_change_password_endpoint))  # Place ?next query param in next form field
#
#     # Process valid POST
#     if request.method=='POST' and form.validate():
#         # Hash password
#         hashed_password = user_manager.hash_password(form.new_password.data)
#
#         # Change password
#         user_manager.update_password(current_user, hashed_password)
#
#         # Send 'password_changed' email
#         if user_manager.enable_email and user_manager.send_password_changed_email:
#             emails.send_password_changed_email(current_user)
#
#         # Send password_changed signal
#         signals.user_changed_password.send(current_app._get_current_object(), user=current_user)
#
#         # Prepare one-time system message
#         flash(_('Your password has been changed successfully.'), 'success')
#
#         # Redirect to 'next' URL
#         return redirect(form.next.data)
#
#     # Process GET or invalid POST
#     return render_template(user_manager.change_password_template, form=form)
#



@user.route('/newuser', methods=['GET', 'POST'])
def newuser_page():
    log.debug('start def newuser_page')
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            log.debug('newuser form.validate()')
            userid = request.form.get('userid')
            newRoles = request.form.get('newRoles')
            functions.setUserRoles(int(userid),newRoles)
            print "roles updated"
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            gsmnr = request.form.get('gsmnr')
            active = request.form.get('active')
            username = request.form.get('username')

            inewuser = functions.setUser(int(userid),username,first_name,last_name,email,gsmnr,active)
            functions.setUserRoles(int(inewuser),newRoles)
            userList = functions.getUserList()
            return render_template('userList.html', tableList=userList, alert=False)
        else:
            log.debug('newuser NOT  form.validate()')
            cuser = functions.getUserDetail(-1)
            croles = functions.getUserRoles(-1)
            return render_template('userdetail.html', cuser=cuser, croles = croles, alert=True)


    log.debug('start def newuser requets')
    cuser = functions.getUserDetail(-1)
    croles = functions.getUserRoles(-1)
    return render_template('userdetail.html', cuser=cuser, croles = croles, alert=False)



@user.route('/userdetail/<userid>', methods=['GET', 'POST'])
def userdetail_page(userid):
    log.debug('start def userdetail_page(userid)')
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            log.debug("userdetailForm : ok")
            userid = request.form.get('userid')
            newRoles = request.form.get('newRoles')
            functions.setUserRoles(int(userid),newRoles)
            log.debug("roles updated")
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            gsmnr = request.form.get('gsmnr')
            active = request.form.get('active')
            username = request.form.get('username')

            functions.setUser(int(userid),username,first_name,last_name,email,gsmnr,active)
            userList = functions.getUserList()
            return render_template('userList.html', tableList=userList, alert=False)
        else:
            log.debug("userdetailForm : NOT ok")
            log.debug("userdetail requets")
            cuser = functions.getUserDetail(userid)
            croles = functions.getUserRoles(userid)
            return render_template('userdetail.html', cuser=cuser, croles = croles, alert=True)

    log.debug("userdetail requets")
    cuser = functions.getUserDetail(userid)
    croles = functions.getUserRoles(userid)
    return render_template('userdetail.html', cuser=cuser, croles = croles, alert=False)


@user.route('/user/profile', methods=['GET', 'POST'])
@login_required
def user_profile_page():
    log.debug("user_profile_page()")
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