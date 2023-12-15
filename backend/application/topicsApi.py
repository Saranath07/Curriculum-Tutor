from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from .models import Questions, Topics, AttemptedQuestions
from flask_jwt_extended.utils import decode_token
from .database import db


class TopicsAPI(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        
        token = request.headers.get('Authorization').split()[1]
        # print(token)
        
        # bearer, token
        decoded_token = decode_token(token)
        
        if decoded_token:
            
            # Get the list of topics
            topics = Topics.query.all()
            
            # Create a list to store the formatted result
            formatted_topics = []

            # Iterate through each topic
            for topic in topics:
                
                # Get the questions associated with the current topic
                questions = Questions.query.filter_by(topic_id=topic.id).all()
                print(questions)
                
                # Format the questions for the current topic
                formatted_questions = []

                for question in questions:
                    
                    attemptQues = AttemptedQuestions.query.filter_by(
                        ques_id = question.ques_id
                    ).first()
                    print(attemptQues)
                    
                    formatted_questions.append(
                        {
                            'qid' : question.ques_id,
                            'attempted' : attemptQues.attempted
                        }
                    )

                # Format the current topic
                formatted_topic = {
                    'tid': topic.id,
                    'name': topic.topic_name,
                    'questions': formatted_questions
                }

                # Append the formatted topic to the result list
                formatted_topics.append(formatted_topic)

            # Return the formatted result
            
            return formatted_topics, 200
        return jsonify({"message": "You are not authorized to perform these actions"}), 400
    
    @jwt_required()
    def post(self):
        token = request.headers.get('Authorization').split()[1]
        # print(token)
        
        # bearer, token
        decoded_token = decode_token(token)

        if not decode_token:
            return "You are not authorized", 400
        
        data = request.get_json()
        
        topic_name = data['topicName']

        topic = Topics(topic_name = topic_name)

        db.session.add(topic)

        db.session.commit()

        return "Topic Added Successfully"

