import requests

# Backend API base URL
BASE_URL = "http://localhost:5000"

# User data for login
login_data = {"email": "me@example.com", "password": "1234"}

# User data for registration
user_data = {"username": "example", "email": "me@example.com", "password": "1234"}

topic_data = {
    "topicName": "Topic 1"
}

# Question data
question_data = {
    "question": "What is the fractional value?",
    "options": "$\\dfrac{1}{3}$, $\\dfrac{1}{2}$, $\\dfrac{2}{9}$",
    "correct_options": "$\\dfrac{1}{2}$",
    "topic": "Topic 1",
    "ques_img" : None,
    "ques_type" : 'Easy'
}

# API endpoints
login_endpoint = f"{BASE_URL}/login"
user_endpoint = f"{BASE_URL}/register/user"
question_endpoint = f"{BASE_URL}/api/questions"
topic_endpoint = f"{BASE_URL}/api/topics"

# Function to make API requests
def make_api_request(endpoint, data, headers=None):
    headers = headers or {}
    headers["Content-Type"] = "application/json"
    response = requests.post(endpoint, json=data, headers=headers)
    return response


# Create user
# user_response = make_api_request(user_endpoint, user_data)
# print("User creation response:", user_response.json())

# Login to obtain access token
login_response = make_api_request(login_endpoint, login_data)
access_token = login_response.json().get("access_token")
headers = {"Authorization": f"Bearer {access_token}"}

# Create topic
topic_response = make_api_request(topic_endpoint, topic_data, headers=headers)
print("Topic creation response:", topic_response.json())

# Create question
question_response = make_api_request(question_endpoint, question_data, headers=headers)
print("Question creation response:", question_response.json)
