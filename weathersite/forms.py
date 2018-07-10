from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from .validators import Unique, IsPasswordMatch
from .models import User

class RegisterForm(Form):
    username = StringField('UserName', validators=[DataRequired(),
        Unique(User, User.UserName, message='There is already an account with that Username.')])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    #, validators=[IsPasswordMatch(password1, password2, message="These passwords do not match")])


class LoginForm(Form):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
