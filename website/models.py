from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')
    executions = db.Column(db.Integer(),default=0)
    date_created = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    lastExecution = db.Column(db.DateTime())
    privileges = db.Column(db.Integer(), default=1)

