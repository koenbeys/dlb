from flask import redirect, render_template, request,url_for, flash
from flask_user import login_required,current_user
from . import user
from .forms import userListForm,userdetailForm
from app import app,db
from . import functions




@user.route('/userList', methods=['GET', 'POST'])
def userList_page():
    form = userListForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "Userlistform : ok"
            userid1 = request.form.get('userid')
            print userid1
            if (int(userid1) > 0):
            #user = functions.getUserDetail(userid)
                return redirect(url_for('user.userdetail_page', userid = userid1))
            else:
                return redirect(url_for('user.newuser_page'))
        else:
            print "Userlistform : not ok"
            userList = functions.getUserList()
            return render_template( 'userlist.html', tableList=userList, alert=True)

    userList = functions.getUserList()
    print "oooo"
    return render_template('userList.html', tableList=userList, alert=False)

@user.route('/newuser', methods=['GET', 'POST'])
def newuser_page():
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "newuser : ok"
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
            print "newuser : NOT ok"
            print "newuser requets"
            cuser = functions.getUserDetail(-1)
            croles = functions.getUserRoles(-1)
            return render_template('userdetail.html', cuser=cuser, croles = croles, alert=True)


    print "newuser requets"
    cuser = functions.getUserDetail(-1)
    croles = functions.getUserRoles(-1)
    return render_template('userdetail.html', cuser=cuser, croles = croles, alert=False)



@user.route('/userdetail/<userid>', methods=['GET', 'POST'])
def userdetail_page(userid):
    form = userdetailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            print "userdetailForm : ok"
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

            functions.setUser(int(userid),username,first_name,last_name,email,gsmnr,active)
            userList = functions.getUserList()
            return render_template('userList.html', tableList=userList, alert=False)
        else:
            print "userdetailForm : NOT ok"
            print "userdetail requets"
            cuser = functions.getUserDetail(userid)
            croles = functions.getUserRoles(userid)
            return render_template('userdetail.html', cuser=cuser, croles = croles, alert=True)


    print "userdetail requets"
    cuser = functions.getUserDetail(userid)
    croles = functions.getUserRoles(userid)
    return render_template('userdetail.html', cuser=cuser, croles = croles, alert=False)
