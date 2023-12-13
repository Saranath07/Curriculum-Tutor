from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topics
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os



qn_fields = {

   "topic": fields.String,
   "question": fields.String,
   "ques_img" : fields.String,
   "ques_type": fields.String,
   "options": fields.String,
   "correct_options": fields.String
  
}

class QuestionsAPI(Resource):
    @jwt_required()
    @marshal_with(qn_fields)
    def get(self,qn_id):
        current_user= get_jwt_identity()

        token = request.headers.get('Authorization').split()[1]
        print(token)
        # bearer, token
        decoded_token = decode_token(token)
        
        
            
        qn = Questions.query.filter_by(qn_id= qn_id).first()
        print(qn)
        return qn
      
        
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        decoded_token = decode_token(token)

        if 'admin' in decoded_token['role']:

            data = request.get_json()
            question = data['question']
            ques_img = data['ques_img']
            ques_type = data['ques_type']
            options = data["options"]
            topic=data['topic']
            correct_options = data["correct_options"]
            print(data)
           
     
            ques = Questions( topic=topic,question= question,  ques_img = ques_img ,  ques_type= ques_type,options= options,
                           correct_options=correct_options)
            
       
            db.session.add(ques)
          
            db.session.commit()

            
            sql4 = Topic(topic = ques.topic, qn_id = ques.ques_id)
            db.session.add(sql4)
            db.session.commit()
   

            return {"message" : "Question created Successfully"}, 200
        else:
            return {'message' : "You are not Authorized to perform this action"}, 400
        
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
       
       
     
            

