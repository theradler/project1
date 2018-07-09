import uuid

from application import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    UserID = db.Column(UUID(as_uuid=True),unique=True, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(64))
    Email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.UserName
