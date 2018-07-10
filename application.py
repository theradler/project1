# import os
# import uuid
#
# from flask import Flask, session, render_template, request, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# from flask_login import LoginManager, current_user, login_user
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
# #from models import User
# #from forms import LoginForm, RegisterForm
# from sqlalchemy.dialects.postgresql import UUID
# from uuid import uuid4
#
# #app = Flask(__name__)
# db = SQLAlchemy()
# login = LoginManager(app)
#
# # Configure session
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# app.config['SECRET_KEY'] = 'passwordkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rfiyeehknxkzti:fcd541969aee3f6c579001a4769f90bb3d27c6e5194c31478217c5010e016a22@ec2-54-227-243-210.compute-1.amazonaws.com:5432/d4dhnjm6dcg7mm'
# Session(app)
#
# # Set up database
# #engine = create_engine(os.getenv("DATABASE_URL"))
# #db = scoped_session(sessionmaker(bind=engine))
# db.init_app(app)
#
# @app.route("/")
# def index():
#     user_session= False
#     return render_template("index.html", user_session=user_session)
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     form = RegisterForm()
#     return render_template('register.html', form=form)
#     if form.validate_on_submit():
#         user = User.query.filter_by(UserName=form.username.data).first()
#         if user is None:
#             db.execute("INSERT INTO User (UserID, UserName, Password) VALUES (:UserId, :UserName, :Password)",
#             {"UserID": uuid4(), "UserName": form.username.data, "Password" : form.password.data })
#             db.commit()
#             return render_template('succes.html')
#         return redirect('fail.html')
#     return render_template('fail.html', title='Register',form=form)
#
# @login.user_loader
# def load_user(id):
#     return User.query.get(UUID(id))
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(UserName=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash("Invalid username or password")
#         login_user(user,remember=form.remember_me.data)
#         return redirect(url_for('index'))
#     return render_template('index.html', title='Sign In', form=form)
#
#
#
# @app.route("/logout")
# def logout():
#     session['logged_in'] = False
#     return index()
#
# if __name__ == "__main__":
#     app.run()
