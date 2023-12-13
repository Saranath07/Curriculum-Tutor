from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from .models import Questions, Topics
from flask_jwt_extended.utils import decode_token

class TopicsAPI(Resource):
    @jwt_required()
    def get(self, topic):
        current_user = get_jwt_identity()
        token = request.headers.get('Authorization').split()[1]
        print(token)
        # bearer, token
        decoded_token = decode_token(token)

        if decode_token:
            # Get the list of topics
            topics = Topics.query.all()

            # Create a list to store the formatted result
            formatted_topics = []

            # Iterate through each topic
            for topic in topics:
                # Get the questions associated with the current topic
                questions = Questions.query.filter_by(topic_id=topic.id).all()

                # Format the questions for the current topic
                formatted_questions = [
                    {
                        'id': question.ques_id,
                        'attempted': False  # You may need to adjust this based on your logic
                    }
                    for question in questions
                ]

                # Format the current topic
                formatted_topic = {
                    'tid': topic.id,
                    'name': topic.topic_name,
                    'questions': formatted_questions
                }

                # Append the formatted topic to the result list
                formatted_topics.append(formatted_topic)

            # Return the formatted result
            return jsonify(formatted_topics), 200
        return "You are not authorized to perform these actions", 400
