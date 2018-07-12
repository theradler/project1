from weathersite import app, db
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import login_user, logout_user, current_user
from uuid import uuid4
from .forms import LoginForm, RegisterForm, SearchForm, CommentForm
from .models import User, Location, Comments
from .utils import darkSkyRequester
import datetime

@app.route("/")
def index():
     user_session= False
     return render_template("index.html", user_session=user_session)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    error = None
    if User.query.filter_by(UserName=form.username.data).count() != 0:
        error = "This username is already in use"
        return render_template('register.html',form=form,error=error)
    if form.password1.data != form.password2.data:
        error = "Your passwords did not match, please try again"
        return render_template('register.html', form=form, error=error)
    if form.validate_on_submit():
        db.session.add(User(UserID = uuid4() ,UserName = form.username.data, Password = form.password1.data ))
        db.session.commit()
        return redirect('/login')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def signin():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(UserName=form.username.data).first_or_404()
        if user.is_correct_password(form.password.data):
            login_user(user)
            return redirect(url_for('search'))
        else:
            error = "Could not log you in, please check you username or password and try again"
            return render_template('login.html', form=form,error=error)
    return render_template('login.html', form=form,error=error)

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    error = None
    if current_user.get_id() is None:
        error = "You must be registered to use this feature, please create and account or sign in"
        return redirect(url_for('register', error=error))
    if form.validate_on_submit():
        column = form.select.data
        search = str.upper(form.search.data)
        if column == 'zipcode':
            results = Location.query.filter(Location.zipcode.like(('%' + search +'%'))).all()
            result_count = Location.query.filter(Location.zipcode.like(('%' + search +'%'))).count()
        elif column == 'city':
            results = Location.query.filter(Location.city.like(('%' + search + '%'))).all()
            result_count = Location.query.filter(Location.city.like(('%' + search + '%'))).count()
        elif column == 'state':
            results = Location.query.filter(Location.state.like(('%' + search + '%'))).all()
            result_count = Location.query.filter(Location.state.like(('%' + search + '%'))).count()
        else:
            return render_template('search.html')
        if result_count == 0:
            error = "No results found, please try again"
            return render_template('search.html',error=error,form=form)
        return render_template('search_results.html', results=results)
    return render_template('search.html', form=form)

@app.route('/search_results', methods=['GET','POST'])
def search_results():
    error = None
    if current_user.get_id() is None:
        error = "You must be registered to use this feature, please create and account or sign in"
        return redirect(url_for('register', error=error))
    return render_template('search_results.html')

@app.route('/location/<string:location_id>')
def location(location_id):
    error = None
    if current_user.get_id() is None:
        error = "You must be registered to use this feature, please create and account or sign in"
        return redirect(url_for('register', error=error))
    form = CommentForm()
    location_data = Location.query.get(location_id)
    weather_data = darkSkyRequester(app.config['DARKSKY_API_KEY'],location_data.latitude, location_data.longitude)
    weather_data = weather_data.getCurrentWeather()
    humidity = str(int(weather_data['humidity'] * 100 )) + "%"
    time =  datetime.datetime.fromtimestamp(weather_data['time']).strftime('%I:%M:%S %p on %Y-%m-%d ')
    comments = Comments.query.filter_by(location_id=location_data.locationid)
    comment_count = Comments.query.filter_by(location_id=location_data.locationid).count()
    current_user_check_ins = Comments.query.filter_by(location_id=location_id,user_id=current_user.get_id()).count()
    return render_template('location.html',location_data=location_data,weather_data=weather_data,form=form,location_id=location_id,time=time,humidity=humidity,comments=comments,comment_count=comment_count,current_user_check_ins=current_user_check_ins)


@app.route('/comment/<string:location_id>/<string:user_id>', methods=['POST'])
def comment(location_id, user_id):
    error = None
    if current_user.get_id() is None:
        error = "You must be registered to use this feature, please create and account or sign in"
        return redirect(url_for('register', error=error))
    form = CommentForm()
    if request.method == 'POST':
        comment = Comments(user_id = user_id,
                           location_id = location_id,
                           comment = form.comment.data
                           )
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('location',location_id=location_id))

@app.route('/api/<string:zip>', methods=['GET'])
def api_request(zip):
    location_data = Location.query.filter_by(zipcode = zip).first()
    if location_data is None:
        return jsonify(error=404), 404
    weather_data = darkSkyRequester(app.config['DARKSKY_API_KEY'],location_data.latitude,location_data.longitude)
    check_ins = Comments.query.filter_by(location_id= location_data.locationid).count()
    response = {
        'place_name': location_data.city,
        'state': location_data.state,
        'latitude': location_data.latitude,
        'longitude': location_data.longitude,
        'zipcode': location_data.zipcode,
        'population': location_data.population,
        'check_ins': check_ins

    }
    return jsonify({'response': response}), 201
