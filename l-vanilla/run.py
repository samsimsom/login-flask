

from flask import request, g, session, make_response
from app import create_app


app = create_app()


@app.before_request
def session_loader():
    session['user'] = 'samsimsom'
