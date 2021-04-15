

from flask import render_template, session
from app.routes.main import main


@main.route('/')
def index():
    title = 'Main'
    return render_template('main/index.html',
                           title=title)
