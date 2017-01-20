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
                    # should be page for password update
                    return redirect(url_for('user.userdetail_page', userid=userid1))

            #
            # if (int(userid1) > 0):
            # #user = functions.getUserDetail(userid)
            #     return redirect(url_for('user.userdetail_page', userid = userid1))
            # else:
            #     return redirect(url_for('user.newuser_page'))
        else:
            print "Userlistform : not ok"
            userList = functions.getUserList()
            return render_template( 'userlist.html', tableList=userList, alert=True)

    userList = functions.getUserList()
    return render_template('userList.html', tableList=userList, alert=False)

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