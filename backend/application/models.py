from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Users(Model):
    id = columns.UUID(primary_key=True)
    public_id = columns.UUID()
    user_name = columns.Text()
    email = columns.Text()
    role = columns.Text()
    password = columns.Text()
    pic = columns.Text()

class Questions(Model):
    ques_id = columns.UUID(primary_key=True)
    question = columns.Text()
    topic = columns.Text()
    category = columns.Text()
    options = columns.List(columns.Text)
    correct_options = columns.List(columns.Text)
    rating = columns.Int()

class Performance(Model):
    perf_id = columns.UUID(primary_key=True)
    user_id = columns.UUID()
    easy = columns.Int()
    medium = columns.Int()
    hard = columns.Int()
    perf_comment = columns.Text()
