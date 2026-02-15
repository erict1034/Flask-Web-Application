from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# This file contains the models for the website.
# It is responsible for defining the database tables
# and the relationships between them.

# The Note model is responsible for storing the notes created by the users.


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# The User model is responsible for storing the users of the website.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
