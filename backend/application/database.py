from sqlalchemy.ext.declarative import declarative_base



from flask.ext.cqlalchemy import CQLAlchemy
engine = None
Base = declarative_base()
db = CQLAlchemy()