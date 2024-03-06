from .database import db

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
    # Establish a one-to-many relationship with AttemptedQuestions
    attempted_questions = db.relationship('AttemptedQuestions', backref='user', lazy='dynamic')

class Topics(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer(), primary_key=True)
    topic_name = db.Column(db.String())
    
    
class Questions(db.Model):
    __tablename__ = "questions"
    
    ques_id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String())
    ques_img = db.Column(db.Text())
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id', ondelete='CASCADE'))
    ques_type = db.Column(db.String())
    options = db.Column(db.String())
    correct_options = db.Column(db.String())
    # Establish a many-to-one relationship with Topics
   
    # Establish a one-to-many relationship with AttemptedQuestions
    attempted_questions = db.relationship('AttemptedQuestions', backref='question', lazy='dynamic')

    
   

class Performance(db.Model):
    __tablename__ = "performance"
    perf_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(), db.ForeignKey('users.id', ondelete='CASCADE'))
    score = db.Column(db.Integer())
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id', ondelete='CASCADE'))
    no_of_questions = db.Column(db.Integer())
    mastery = db.Column(db.Boolean, default=None)

class AttemptedQuestions(db.Model):
    __tablename__ = "attempted_questions"
    attemptques_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    ques_id = db.Column(db.Integer, db.ForeignKey('questions.ques_id', ondelete='CASCADE'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id', ondelete='CASCADE'))
    attempted = db.Column(db.Boolean, default=False)
    status = db.Column(db.Boolean, default=None)
    options = db.Column(db.String())

    # Add a unique constraint on user_id and ques_id
    __table_args__ = (db.UniqueConstraint('user_id', 'ques_id'),)

    def __init__(self, user_id, ques_id, topic_id, attempted, status, options):
        self.user_id = user_id
        self.ques_id = ques_id
        self.topic_id = topic_id
        self.attempted = attempted
        self.status = status
        self.options = options
    # Add a column to store the attempt status (True/False)
        




# class indi_perf(db.Model):
#     __tablename__ = "indi-perf"
#     user_id = db.Column(db.String(), db.ForeignKey('users.id' , ondelete='CASCADE'))
#     qn_id = db.Column(db.String(), db.ForeignKey('questions.ques_id' , ondelete='CASCADE'))
#     select_options = db.Column(db.String())
#     correct_options = db.Column(db.String())
#     marks = db.Column(db.Integer())
    

# scores, user_d, topic_id, mastered
# db.create_all()