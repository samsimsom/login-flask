

from flask import render_template
from app.routes.user import user


@user.route('/')
def index():
    title = 'User'
    return render_template('user/index.html',
                           title=title)
