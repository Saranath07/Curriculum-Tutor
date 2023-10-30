from flask import jsonify, request, current_app as app
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.auth import PlainTextAuthProvider
import uuid
import time

# Connect to your Cassandra cluster
cluster = Cluster(
    contact_points=['your_cassandra_host'],  # Provide the Cassandra cluster host
    auth_provider=PlainTextAuthProvider(username='your_cassandra_username', password='your_cassandra_password')
)
session = cluster.connect('your_keyspace')  # Provide your Cassandra keyspace

# Define your Cassandra model
class Users(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    public_id = columns.UUID()
    user_name = columns.Text()
    email = columns.Text()
    role = columns.Text()
    password = columns.Text()
    pic = columns.Text()

# Sync the Cassandra model with the database
sync_table(Users)

@app.route('/register/user', methods=["POST"])
@cross_origin()
def register_user():
    data = request.get_json()
    hash_pwd = generate_password_hash(data['password'], method='pbkdf2:sha256:200000', salt_length=16)
    new_user = Users(public_id=uuid.uuid4(), user_name=data['username'], password=hash_pwd, email=data['email'], role='user')
    new_user.save()
    return jsonify({"message": "User registered successfully"})

@app.route('/register/admin', methods=["POST"])
@cross_origin()
def register_admin():
    data = request.get_json()
    hash_pwd = generate_password_hash(data['password'], method='pbkdf2:sha256:200000', salt_length=16)
    new_user = Users(public_id=uuid.uuid4(), user_name=data['username'], password=hash_pwd, email=data['email'], role='admin')
    new_user.save()
    return jsonify({"message": "Admin registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    uname = data.get("username")
    password = data.get("password")
    user = Users.objects.filter(user_name=uname).first()

    if user and check_password_hash(user.password, password):
        user.lastseen = time.time()  # Update the lastseen property
        user.save()
        # You'll need to implement JWT authentication for Cassandra separately
        # Create an access token and return it
        access_token = create_access_token(identity=str(user.public_id), additional_claims={'role': user.role})
        return jsonify({"access_token": access_token, "username": user.user_name, "role": user.role}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
