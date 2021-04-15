

from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_app(applicaiton):
    db.init_app(app=applicaiton)
