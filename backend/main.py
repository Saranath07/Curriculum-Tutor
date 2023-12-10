import os
from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from flask_cors import CORS
from application.database import db
#  from application.login import *
from flask_jwt_extended import JWTManager

from application.models import *
from application.userAPI import *
from application.questionAPI import *



CELERY_BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
app = None
api = None
celery = None
app = None
api = None
celery = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    print(os.getenv('ENV', "development"))
    if os.getenv('ENV', "development") == "production":
      app.logger.info("Currently no production config is setup.")
      raise Exception("Currently no production config is setup.")
    
    else:
      app.logger.info("Staring Local Development.")
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
      print("pushed config")
    # app.app_context().push()
    print("DB Init")
    db.init_app(app)
    print("DB Init complete")
    app.app_context().push()
    app.logger.info("App setup complete")
    # Setup Flask-Security
    
    api = Api(app)
   
    app.app_context().push()   
    
    # Create celery   





    print("Create app complete")
    return app, api

app, api = create_app()





cors = CORS(app) 
api = Api(app)

jwt = JWTManager(app)
with app.app_context():
    db.create_all()


from application.login import *

api.add_resource(UserApi,"/api/user_profile")
api.add_resource(QuestionsAPI,"/api/questions","/api/questions/<topic>")

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
        app.run(debug=True)