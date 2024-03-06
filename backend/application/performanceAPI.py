from flask_restful import Resource
from flask import request
from .database import db
from .models import Topics, AttemptedQuestions, Users, Performance
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended.utils import decode_token
import os
from collections import defaultdict
import math





def user_topic_correctness(user, topic_id, w):
  
    """
    Calculates the number of correct answers for the last w attempted questions for each topic of the user.

    Args:
        user: The user object.
        w: The number of most recent questions to consider.

    Returns:
        A dictionary where keys are topics (Topic objects) and values are integers representing 
        the number of correct answers in the last w attempted questions for each topic.

    """

    # Use defaultdict to create an empty dictionary with Topic objects as keys
    s = 0

    # Filter attempted questions by user
    
    attempted_ques = AttemptedQuestions.query.filter_by(user_id=user.id, topic_id = topic_id).all()

    attempted_ques = list(reversed(attempted_ques))
    print(attempted_ques)
    # Iterate through each attempted question
    i = 0
    for question in attempted_ques:
        # Check if it falls within the last w questions based on a counter
        if i < w:
            s += question.status
            i += 1

    return s



def masteryDetection(user, topic_id, w, h):
    
    u = user_topic_correctness(user, topic_id, w)
    print(u, math.ceil(w * h))
    if u > math.ceil(w * h):
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
            userPerf.mastery = masteryDetection(user, topic.id, w=6, h=0.75)
    
            json = {
                "name" : topic.topic_name,
                "questionsSolved" : userPerf.no_of_questions,
                "mastered" : userPerf.mastery,
                "correct_questions" : userPerf.score
            }
            outjson.append(json)
        
        return outjson
        

