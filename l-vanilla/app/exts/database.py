
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface

db = MongoEngine()


def init_app(applicaiton):
    db.init_app(app=applicaiton)


def session_interface(database):
    return MongoEngineSessionInterface(database)
