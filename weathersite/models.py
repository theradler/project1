from weathersite import db
from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    UserID = db.Column(UUID(as_uuid=True),unique=True, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(64))

    def is_correct_password(self, plaintext):
        return self.Password == plaintext

    def is_active(self):
        return True

    def get_id(self):
        return self.UserID

    def is_authenticated(self):
        return True

    def __repr__(self):
        return  self.UserName

class Location(db.Model):
    __tablename__ = 'location'
    __searchable__ = ['Zipcode','City','State']
    locationid = db.Column(UUID(as_uuid=True),unique=True, primary_key=True)
    zipcode = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    population = db.Column(db.Integer())

    def __repr__(self):
        return '<City: %r>' % self.city


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(User.UserID))
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Location.locationid))
    comment = db.Column(db.String())
    user_name = db.relationship("User",backref="Comments",lazy=True)

    def __repr__(self):
        return '<Comment: %r>' % self.comment
