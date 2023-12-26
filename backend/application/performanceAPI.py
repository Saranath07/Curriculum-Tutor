from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topics, AttemptedQuestions, Users, Performance
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os


class PerformanceAPI(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()

        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)

        if not decoded_token:
            return "Authorization Error", 404
        
        user = Users.query.filter_by(public_id = current_user).first()

        userPerfs = Performance.query.filter_by(user_id = user.id).all()

        outjson = []

        for userPerf in userPerfs:
            topic = Topics.query.filter_by(id = userPerf.topic_id).first()
            json = {
                "name" : topic.topic_name,
                "questionsSolved" : userPerf.no_of_questions,
                "mastered" : userPerf.mastery
            }
            outjson.append(json)
        
        return outjson
        

