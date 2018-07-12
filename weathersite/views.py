from weathersite import app, db
from flask import session, render_template, request, redirect, url_for, abort, jsonify
from flask_login import login_user, logout_user
from uuid import uuid4
from .forms import LoginForm, RegisterForm, SearchForm, CommentForm
from .models import User, Location, Comments
from .utils import darkSkyRequester

@app.route("/")
def index():
     user_session= False
     return render_template("index.html", user_session=user_session)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
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
            return redirect(url_for('search'))
        else:
            return redirect(url_for('register'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/search', methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        column = form.select.data
        search = str.upper(form.search.data)
        if column == 'zipcode':
            results = Location.query.filter(Location.zipcode.like(('%' + search +'%'))).all()
        elif column == 'city':
            results = Location.query.filter(Location.city.like(('%' + search + '%'))).all()
        elif column == 'state':
            results = Location.query.filter(Location.state.like(('%' + search + '%'))).all()
        else:
            return  render_template('search.html')
        return render_template('search_results.html', results=results)
    return render_template('search.html', form=form)

@app.route('/search_results', methods=['GET','POST'])
def search_results():
    return render_template('search_results.html')

@app.route('/location/<string:location_id>')
def location(location_id):
    form = CommentForm()
    location_data = Location.query.get(location_id)
    weather_data = darkSkyRequester(app.config['DARKSKY_API_KEY'],location_data.latitude, location_data.longitude)
    weather_data = weather_data.getCurrentWeather()
    return render_template('location.html',location_data=location_data,weather_data=weather_data,form=form,location_id=location_id)


@app.route('/comment/<string:location_id>/<string:user_id>', methods=['POST'])
def comment(location_id, user_id):
    form = CommentForm()
    if request.method == 'POST':
        comment = Comments(user_id = user_id,
                           location_id = location_id,
                           comment = form.comment.data
                           )
        db.session.add(comment)
        db.session.commit()
    return render_template('location.html',form=form)

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
