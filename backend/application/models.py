from .database import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    stud_name = db.Column(db.String())
    # std = db.Column(db.Integer())
    email = db.Column(db.String())
    role = db.Column(db.String())

class questions(db.Model):
    __tablename__ = 'question'
    ques_id = db.Column