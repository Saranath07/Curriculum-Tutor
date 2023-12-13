from flask import jsonify, request
from flask import current_app as app
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import uuid
import time
from .database import db
from .models import Users
from flask_jwt_extended import  jwt_required, create_access_token

@app.route('/register/user',methods=["POST"])
@cross_origin()
def register_user():
    data = request.get_json()
    hash_pwd = generate_password_hash(data['password'],method = 'pbkdf2:sha256')
    new_user = Users(public_id = str(uuid.uuid4()),user_name = data['username'],password = hash_pwd,email=data['email'], role='user')
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User registered successfully", "user" : new_user.user_name})

@app.route('/register/admin',methods=["POST"])
@cross_origin()
def register_admin():
    data = request.get_json()
    hash_pwd = generate_password_hash(data['password'],method = 'pbkdf2:sha256')
    new_user = Users(public_id = str(uuid.uuid4()),password = hash_pwd ,user_name = data['username'],email=data['email'],role='admin')
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"Admin registered successfully"})

@app.route("/login",methods=["POST"])
def login():
   
    data = request.get_json()
    print(data)
   
    email = data.get("email")
    password = data.get("password")

    print(email)
    
    user = Users.query.filter_by(email=email).first()
    print(user)
    if not user:
        return jsonify({"error":" Please signup"}), 404
    
    if check_password_hash(user.password,password):
        # user.lastseen=time.time()
        db.session.commit()
        access_token = create_access_token(identity= user.public_id,additional_claims  = {'role':user.role})
        return jsonify({"access_token":access_token, "username":user.user_name,"role":user.role}),200
    else:
        return jsonify({"error":" Could not login"}), 404

