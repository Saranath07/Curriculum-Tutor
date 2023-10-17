from .database import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    user_name = db.Column(db.String())
    email = db.Column(db.String())
    role = db.Column(db.String())
    # performance = db.Column(db.String())
    password = db.Column(db.String())
    pic = db.Column(db.String())

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer(),primary_key=True)
    question = db.Column(db.String())
    topic = db.Column(db.String())
    category = db.Column(db.String())
    options = db.Column(db.String())
    correct_options = db.Column(db.String())
    rating = db.Column(db.Integer())

class Performance(db.Model):
    __tablename__ = 'performance'
    perf_id = db.Column(db.Integer(),primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id, ondelete='CASCADE'))
    easy = db.Column(db.Integer())
    medium = db.Column(db.Integer())
    hard = db.Column(db.Integer())
    performance = db.Column(db.String())






