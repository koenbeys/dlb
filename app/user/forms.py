from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, IntegerField, BooleanField,PasswordField
from flask_user.forms import RegisterForm
from . import log

#    , DateField, DateTimeField, TextField FloatField, PasswordField,


class LoginForm(Form):
    username = StringField('User--', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])


# Define the User profile form
class UserProfileForm(Form):
    log.debug('start class UserProfileForm')
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')
    submit = SubmitField('Save')


class userListForm(Form):
    log.debug('start class userListForm')
    userid = IntegerField('userid') #, validators=[
        #validators.DataRequired('id is required')])
    op = StringField('op', validators=[
        validators.DataRequired('Op is required')])
    # print "valid"
    submit = SubmitField('Submit')

class userdetailForm(Form):
    log.debug('start class userdetailForm')
    userid = IntegerField('userid', validators=[
        validators.DataRequired('First name is required')])
    newRoles = StringField('newRoles', validators=[
        validators.DataRequired('First name is required')])
    first_name = StringField('first_name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('last_name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')
    email = StringField('email', validators=[
        validators.DataRequired('email is required')])
    username = StringField('username', validators=[
        validators.DataRequired('username is required')])
    active =  BooleanField(u'active')
    # print "valide"

class MyRegisterForm(RegisterForm):
    log.debug('start class MyRegisterForm')
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')