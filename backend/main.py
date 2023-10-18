import os
from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from flask_cors import CORS
from application.database import db


from flask_jwt_extended import JWTManager
from application.models import Users



# CELERY_BROKER_URL = "redis://localhost:6379/1"
# CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
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
    app.app_context().push()
    print("DB Init")
    db.init_app(app)
    print("DB Init complete")
    app.app_context().push()
    app.logger.info("App setup complete")
    # Setup Flask-Security
    
    api = Api(app)
    app.app_context().push()   
    
    # Create celery   
    # celery = workers.celery

    # Update with configuration
    # celery.conf.update(
    #     broker_url = app.config["CELERY_BROKER_URL"],
    #     result_backend = app.config["CELERY_RESULT_BACKEND"]
    # )

    # celery.Task = workers.ContextTask
    # app.app_context().push()
    print("Create app complete")
    return app, api

app, api = create_app()

from application.login import *

app, api = create_app()

cors = CORS(app) # Allow cross-origin requests
api = Api(app)

jwt = JWTManager(app)
with app.app_context():
    db.create_all()










if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
