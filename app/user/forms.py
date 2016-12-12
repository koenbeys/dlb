from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, IntegerField, BooleanField
from flask_user.forms import RegisterForm

#    , DateField, DateTimeField, TextField FloatField, PasswordField,

# Define the User profile form
class UserProfileForm(Form):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')
    submit = SubmitField('Save')


class userListForm(Form):
    userid = IntegerField('userid') #, validators=[
        #validators.DataRequired('id is required')])
    # print "valid"
    submit = SubmitField('Submit')

class userdetailForm(Form):
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
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')