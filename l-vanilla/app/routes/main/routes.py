

from flask import render_template, session
from app.routes.main import main


@main.route('/')
def index():
    title = 'Main'
    session['test'] = 'test'
    return render_template('main/index.html',
                           title=title)

@main.route('/clear')
def clear():
    session.clear()
    return 'Clear'
