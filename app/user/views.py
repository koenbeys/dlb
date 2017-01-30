from flask import redirect, render_template, request,url_for, flash, get_flashed_messages
from flask_user import login_required,current_user
# from flask_login import login_user,abort
# from .functions import is_safe_url
from . import user,log
from .forms import userdetailForm,LoginForm,UserProfileForm, userListForm, SetPasswordForm
from app import app,db
from . import functions

@user.route('/userList', methods=['GET', 'POST'])
def userList_page():
    log.debug('start def userList_page')
    form = userListForm(request.form)
    log.debug('form')
    if request.method == 'POST':
        log.debug("request.method == 'POST'     => True")
        if form.validate():
            log.debug("form.validate()     => True")
            userid1 = request.form.get('userid')
            op = request.form.get('op')
            log.debug("userid = '%s', op = '%s'",userid1,op)

            if (op == "new"):
                print "new"
                return redirect(url_for('user.newuser_page'))
            else:
                if (op == "edit"):
                    print "user edit"
                    return redirect(url_for('user.userdetail_page', userid=userid1))
                    # cuser = functions.getUserDetail(userid1)
                    # croles = functions.getUserRoles(userid1)
                    #
                    # return render_template('userdetail.html', cuser=cuser, croles=croles)

                else:
                    print "password update"
                    # should be page for password update

                    # return redirect(url_for('user.set_password', userid=userid1))
                    cuser = functions.getUserDetail(userid1)
                    forma = SetPasswordForm(request.form)
                    return render_template('set_passwd.html',form=forma, userid=userid1, cuser=cuser)

                    # return redirect(url_for('user.set_password_page', userid=userid1))
        else:
            log.debug("form.validate()     => False")
            userList = functions.getUserList()
            log.debug("na userList")
            return render_template( 'userlist.html', tableList=userList, alert=True)
    else:
        log.debug("if request.method == 'POST' => False" )
        userList = functions.getUserList()
        log.debug("na userList")

        return render_template('userList.html', tableList=userList, alert=False)


@user.route('/userdetail/<userid>', methods=['GET', 'POST'])
def userdetail_page(userid):
    log.debug('start def userdetail_page(userid)')
    form = userdetailForm(request.form)
    print "jjj"
    print request.form.get('formname')
    if request.form.get('formname')=='userdetail':
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
                # return render_template('userList.html', tableList=userList, alert=False)
                return redirect(url_for('user.userList_page'))

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





@user.route('/set_password/<userid>', methods=['GET', 'POST'])
def set_password(userid):
    print userid
    form = SetPasswordForm(request.form)
    return render_template('set_passwd.html', form=form)

    app.user_manager
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