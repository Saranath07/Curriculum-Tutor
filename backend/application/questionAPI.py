from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topics, AttemptedQuestions, Users
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os




class QuestionsAPI(Resource):
    @jwt_required()
    def get(self, id):
        current_user = get_jwt_identity()

        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)

        if decoded_token:
            user = Users.query.filter_by(public_id = current_user).first()
            qn = Questions.query.filter_by(ques_id=id).first()

            # Get attempted question details for the current user and question
            attempted_qn = AttemptedQuestions.query.filter_by(
                user_id=user.id,
                ques_id=id
            ).first()
            val1 = False
            val2 = None
            val3 = None
            if attempted_qn:
                val1 = attempted_qn.attempted
                val2 = attempted_qn.status
                val3 = qn.correct_options
            
            # Combine question details and attempted question details in the response
            response = {
                "topic": qn.topic_id,
                "question": qn.question,
                "ques_img": qn.ques_img,
                "ques_type": qn.ques_type,
                "options": qn.options,
                "attempted" : val1,
                "status" : val2,
                "correct_option" : val3
            }
            print(response)
            return response

        return "You are not authorized", 400
        
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)

        

        data = request.get_json()
        question = data['question']
        ques_img = data['ques_img']
        ques_type = data['ques_type']
        options = data["options"]
        topicname=data['topic']
        topic = Topics.query.filter_by(topic_name = topicname).first()
        correct_options = data["correct_options"]
        print(topic)
        
    
        ques = Questions( topic_id = topic.id,question= question,  ques_img = ques_img ,  ques_type= ques_type,options= options,
                        correct_options=correct_options)
        
    
        db.session.add(ques)
        
        db.session.commit()

        
        # sql4 = Topic(topic = ques.topic, qn_id = ques.ques_id)
        # db.session.add(sql4)
        # db.session.commit()


        return {"message" : "Question created Successfully"}, 200
        
        
    @jwt_required()
    def put(self,qn_id):
        
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)

        if 'admin' in decoded_token['role']:
            data = request.get_json()
            quest = data['question']

            sql = db.session.query(Questions).filter(Questions.ques_id == qn_id).first()

            if sql is None:
                return jsonify({'message': 'Question not found'}), 404

            sql.question = quest
            db.session.commit()
        return "Question edited successfully"
    
        
    def delete(self, qn_id):
  
     
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]  
        

        decoded_token = decode_token(token)
       
        if 'admin' in decoded_token['role']:
          
            qn = Questions.query.filter_by(ques_id=qn_id).first()
            if qn :
                db.session.delete(qn)
                db.session.commit()
                return {'message' : "Deleted Successfully"}
        return {'message' : "Not Deleted"}
       
       
     
            

