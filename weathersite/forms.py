from flask_wtf import Form
from wtforms import StringField, PasswordField,  SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired

from .validators import Unique, IsPasswordMatch
from .models import User

class RegisterForm(Form):
    username = StringField('Enter a UserName: ', validators=[DataRequired(),
        Unique(User, User.UserName, message='There is already an account with that Username.')])
    password1 = PasswordField('Enter Password', validators=[DataRequired()])
    password2 = PasswordField('Re-Enter Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    #, validators=[IsPasswordMatch(password1, password2, message="These passwords do not match")])


class LoginForm(Form):
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SearchForm(Form):
    choices = [('zipcode', 'Zipcode'),
               ('city','City'),
               ('state','State')]
    select = SelectField('Choose your search criteria', choices=choices)
    search = StringField('Enter you search value')
    submit = SubmitField('Let her rip')


class CommentForm(Form):
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Check In')