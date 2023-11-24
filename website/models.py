from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(300))
    first_name = db.Column(db.String(150))
    date_registr = db.Column(db.DateTime(timezone=True), default=func.now())
    notes = db.relationship('Notes')
