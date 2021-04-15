

from flask import session
from app import create_app


app = create_app()


@app.before_request
def initialize():
    if session.get('user') is None:
        session['user'] = {'id': None,
                           'username': None,
                           'email': None,
                           'slug': None}


@app.context_processor
def get_current_user():
    return dict(current_user=session['user'])
