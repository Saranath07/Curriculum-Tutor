from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topics, AttemptedQuestions, Users, Performance
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os


class EvaluateAPI(Resource):

    @jwt_required()
    def post(self, id):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        print(token)
        # bearer, token
        decoded_token = decode_token(token)
        if not decoded_token:
            return {"message" : "Not Authorized to do this action"}, 404
        
        question = Questions.query.filter_by(ques_id = id).first()
        data = request.get_json()

        studentOption = data['studentOption']
        
        print(f"Student Option : {studentOption}")
        
        current_user = Users.query.filter_by(public_id=current_user).first()
        print(current_user.id)
        
        print(question.correct_options, studentOption)
        if question.correct_options == studentOption.strip():
            stud_data = AttemptedQuestions(user_id = current_user.id, ques_id = id, attempted = True, status = True, 
                                           options = studentOption, topic_id = question.topic_id)
            try:
                db.session.add(stud_data)
                exist_perf = Performance.query.filter_by(user_id = current_user.id, topic_id = question.topic_id).first()
                if exist_perf:
                    exist_perf.score += 1
                    exist_perf.no_of_questions += 1
                else:
                    perf = Performance(user_id = current_user.id, topic_id = question.topic_id, score = 1, no_of_questions = 1)
                    db.session.add(perf)
                db.session.commit()
                return "Perfect!!", 200
            except:
                return "You cannot attempt once again", 404
        else:
            stud_data = AttemptedQuestions(user_id = current_user.id, ques_id = id, attempted = True, 
                                           status = False, options = studentOption, topic_id = question.topic_id)
            try:
                db.session.add(stud_data)
                db.session.add(stud_data)
                exist_perf = Performance.query.filter_by(user_id = current_user.id, topic_id = question.topic_id).first()
                if exist_perf:
                    
                    exist_perf.no_of_questions += 1
                else:
                    perf = Performance(user_id = current_user.id, topic_id = question.topic_id, score = 0, no_of_questions = 1)
                    db.session.add(perf)
                db.session.commit()
               
                return {"message" : "You have a mistake", "correct_option" : question.correct_options}, 200
            except:
                return "You cannot attempt once again", 404
        
        
