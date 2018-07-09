import uuid

from application import db, login
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID



class User(UserMixin, db.Model):
    UserID = db.Column(UUID(as_uuid=True),unique=True, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(64))
    
    def __repr__(self):
        return '<User %r>' % self.UserName

class Location(db.Model):
    locatioID = db.Column(UUID(as_uuid=True),unique=True, primary_key=True)
    Zipcode = db.Column(db.Integer(), unique=True)
    City = db.Column(db.String(64),unique=True)
    State = db.Column(db.String(64))
    Latitude = db.Column(db.Integer())
    Longitude = db.Column(db.Integer())
