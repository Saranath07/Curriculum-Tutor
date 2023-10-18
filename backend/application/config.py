import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    MAIL_USERNAME = "ENTER YOUR EMAIL HERE"
    MAIL_PASSWORD = "ENTER PW HERE"
    SQLALCHEMY_DB_DIR = os.path.join(basedir, "/db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///project_example.sqlite3"
    DEBUG = True
    JWT_SECRET_KEY = 'super-secret' # Change this to your own secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CORS_HEADERS = 'Content-Type'
    WTF_CSRF_ENABLED = False
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    SMPTP_SERVER_HOST = "localhost"
    SMPTP_SERVER_PORT = 1025
    SENDER_ADDRESS = "email@example.com"
    SENDER_PASSWORD = ""

class ProjectDevelopmentConfig(Config):
    SQLALCHEMY_DB_DIR = os.path.join(basedir, "/db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLALCHEMY_DB_DIR, "project_example.sqlite3")
    JWT_SECRET_KEY = 'super-secret' # Change this to your own secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CORS_HEADERS = 'Content-Type' 
    
    DEBUG = False
    