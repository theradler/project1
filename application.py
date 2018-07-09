import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("postgres://rfiyeehknxkzti:fcd541969aee3f6c579001a4769f90bb3d27c6e5194c31478217c5010e016a22@ec2-54-227-243-210.compute-1.amazonaws.com:5432/d4dhnjm6dcg7mm"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://rfiyeehknxkzti:fcd541969aee3f6c579001a4769f90bb3d27c6e5194c31478217c5010e016a22@ec2-54-227-243-210.compute-1.amazonaws.com:5432/d4dhnjm6dcg7mm"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")

def index():
    user_session= False
    return render_template("index.html", user_session=user_session)

@app.route("/register")
def register():
    return render_template("register.html")
