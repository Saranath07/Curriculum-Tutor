from .database import db
# from sqlalchemy import Column, Integer, String
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String())
    user_name = db.Column(db.String())
    email = db.Column(db.String())
    role = db.Column(db.String())
    password = db.Column(db.String())
    pic = db.Column(db.String())
    gender = db.Column(db.String())

class Questions(db.Model):
    __tablename__ = "questions"
    
    ques_id = db.Column(db.Integer(),primary_key=True)
    question = db.Column(db.String())
    ques_img = db.Column(db.Text())
    topic = db.Column(db.String())
    ques_type = db.Column(db.String())
    options = db.Column(db.String())
    correct_options = db.Column(db.String())
 


class Performance(db.Model):
    __tablename__ = "performance"
    perf_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), db.ForeignKey('users.id' , ondelete='CASCADE'))
    score = db.Column(db.Integer())
    topic_id = db.Column(db.String())
    mastery = db.Column(db.String())

# scores, user_d, topic_id, mastered
# db.create_all()