from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topics, AttemptedQuestions, Users, Performance
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os

'''
The logic for mastery detection is as follows:

w: window size ( w can be set as 8)
h: accuracy threshold (h can be set as 0.75)

if the number of responses by a student for a topic  >= w:
    consider the number of correct responses (c) in the last w responses
    compute f = c/w
    if f>h:
     mastery = True

'''

def masteryDetection(userPerf, w, h):
     
    
    n = userPerf.no_of_questions
    c = userPerf.score

    if n >= w:
        f = c / w
        if f > h:
            return True

    return False

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
            userPerf.mastery = masteryDetection(userPerf, w=6, h=0.75)
            json = {
                "name" : topic.topic_name,
                "questionsSolved" : userPerf.no_of_questions,
                "mastered" : userPerf.mastery,
                "correct_questions" : userPerf.score
            }
            outjson.append(json)
        
        return outjson
        

