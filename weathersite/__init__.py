
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)



#Load Configuration
app.config.from_pyfile('..\config.py')


#Configure Database Session
db = SQLAlchemy()
db.init_app(app)


import weathersite.views



from .models import User
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sign in"

@login_manager.user_loader
def load_user(userid):
    return User.query.filter(User.UserID==userid).first()
