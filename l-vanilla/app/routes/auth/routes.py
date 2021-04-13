

from flask import render_template
from app.routes.auth import auth


@auth.route('/')
def index():
    title = 'Auth'
    return render_template('auth/index.html',
                           title=title)
