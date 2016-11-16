from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,validators,SelectField
from flask_user.forms import RegisterForm


# Define the User profile form
class UserProfileForm(Form):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')
    submit = SubmitField('Save')

class RoleForm(Form):
        myChoices = (("koen","koen"),("piet","piet"),("jan","jaan")) # number of choices
        myField = SelectField(u'Field name', choices=myChoices, validators=[validators.DataRequired()])

'''
    name = StringField('Role name', validators=[
        validators.DataRequired('Role name is required')])
    label = StringField('Label ', validators=[
        validators.DataRequired('Label is required')])
    submit = SubmitField('Save')
'''
class MyRegisterForm(RegisterForm):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
    gsmnr = StringField('gsmnr')

'''
class LoginForm(Form):
    username = StringField('User', validators=[validators.DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[validators.DataRequired()])
'''
