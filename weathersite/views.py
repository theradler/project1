from weathersite import app, db
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from uuid import uuid4
from .forms import LoginForm, RegisterForm
from .models import User

@app.route("/")
def index():
     user_session= False
     return render_template("index.html", user_session=user_session)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # connection = db.get_engine(app).connect()
        # connection.execute('SELECT * FROM user')
        # # connection.execute('INSERT INTO user (UserID, UserName, Password) VALUES (:UserID, :UserName, :Password)', {"UserID" : uuid4(), "UserName" : form.username.data, "Password" : form.password1.data  })
        # connection.commit()
        db.session.add(User(UserID = uuid4() ,UserName = form.username.data, Password = form.password1.data ))
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(UserName=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)

            return redirect(url_for('searchhome'))
        else:
            return redirect(url_for('register'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/searchhome')
def searchhome():
    return render_template("searchhome.html")
