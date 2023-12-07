from flask_restful import Resource, marshal_with, fields
from flask import request
from .database import db
import uuid
from flask import jsonify
from .models import Questions
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
    def get(self,topic):
        current_user= get_jwt_identity()

        token = request.headers.get('Authorization').split()[1]
        # bearer, token
        decoded_token = decode_token(token)
        if 'admin' in  decoded_token['role']:
        
            
            qn = Questions.query.filter_by(topic= topic).all()
            print(qn)
            return qn
      
        return {'message' : "You are not Authorized to perform this action"}, 400
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
            return {"message" : "Question created Successfully"}, 200
        else:
            return {'message' : "You are not Authorized to perform this action"}, 400
        
    # @jwt_required()
    # def put(self,the_id):
    #     current_user = get_jwt_identity()
    #     token = request.headers.get('Authorization').split()[1]
    #     decoded_token = decode_token(token)

    #     if 'admin' in decoded_token['role']:
    #         data = request.get_json()
    #         the_name = data['the_name']

    #         sql = db.session.query(Theatre).filter(Theatre.the_id == the_id).first()

    #         if sql is None:
    #             return jsonify({'message': 'Theatre not found'}), 404

    #         sql.the_name = the_name
    #         db.session.commit()
    #     return "Theatre edited successfully"
    
        
    # def delete(self, the_id):
    #     # return "Hello", 200
    #     verify_jwt_in_request()
    #     current_user = get_jwt_identity()
    #     token = request.headers.get('Authorization').split()[1]  
        

    #     decoded_token = decode_token(token)
       
    #     if 'admin' in decoded_token['role']:
          
    #         the_mov = TheatreMovie.query.filter_by(the_id=the_id).all()
    #         book = Bookings.query.all()
    #         l = []
    #         for i in the_mov:
    #             l.append(i.id)
    #         for j in book:
    #             if j.movie_the_id in l:
    #                 db.session.delete(j)
    #         db.session.commit()
     
            

    #         theatre = Theatre.query.filter_by(the_id = the_id).first() 
      
         
    #         db.session.delete(theatre)

    #         db.session.commit()
    #         the_mov = TheatreMovie.query.filter_by(the_id=the_id).all()
    #         for k in the_mov:
    #             db.session.delete(k)
    #         db.session.commit()
    #         return {"message" : "Theatre Deleted Successfully"}, 200
    #     else:
    #         return {'message' : "You are not Authorized to perform this action"}, 400
    
