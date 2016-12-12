from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,validators,SelectField





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


'''
class LoginForm(Form):
    username = StringField('User', validators=[validators.DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[validators.DataRequired()])
'''
