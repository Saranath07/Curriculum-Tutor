from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions, Topic
from flask_jwt_extended import jwt_required, verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os



qn_fields = {

   "topic": fields.String,
   "question": fields.String,
   "ques_img" : fields.String,
   "ques_type": fields.String,
   "options": fields.String,
  
}

class TopicAPI(Resource):
    @jwt_required()
    @marshal_with(qn_fields)
    def get(self,topic_id):
        current_user= get_jwt_identity()

        token = request.headers.get('Authorization').split()[1]
        print(token)
        # bearer, token
        decoded_token = decode_token(token)
        
        
            
        topic_qns =Topic.query.filter_by(topic_id = topic_id).all()
        L = []
        for i in topic_qns:
            m = Questions.query.filter_by(qn_id= i.qn_id).first()
            L.append(m)
        print(L)
        return L
      

    
        
    def delete(self, topic_id):
  
     
        verify_jwt_in_request()
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]  
        

        decoded_token = decode_token(token)
       
        if 'admin' in decoded_token['role']:
          
            top = Topic.query.filter_by(topic_id=topic_id).first()
            if top :
                db.session.delete(top)
                db.session.commit()
                return {'message' : "Topic Deleted Successfully"}
        return {'message' : "Topic Not Deleted"}
       
       
     
            

