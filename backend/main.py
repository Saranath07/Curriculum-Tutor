import os
from flask import Flask
from flask_restful import Api
from application.config import LocalDevelopmentConfig
from flask_cors import CORS
from application.database import db
from flask_jwt_extended import JWTManager
from application.models import Users
from application import workers
from celery.schedules import timedelta
from flask_sse import sse

app = None
api = None
celery = None
def create_app():
    
    app = Flask(__name__)
    if os.getenv("ENV","development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    
    
    api = Api(app)
    app.app_context().push()
    celery = workers.celery
    celery.conf.update(
        broker_url = app.config["CELERY_BROKER_URL"],
        result_backend = app.config["CELERY_RESULT_BACKEND"]
    )
    celery.Task = workers.ContextTask
    app.app_context().push()
    
    
    return app, api, celery

app, api, celery = create_app()

cors = CORS(app) # Allow cross-origin requests 
api = Api(app)

jwt = JWTManager(app)
with app.app_context():
    db.create_all()

app.register_blueprint(sse, url_prefix='/stream')










if __name__ == "__main__":
    
    app.run(
        debug = True,
        
    )
