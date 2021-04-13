

from flask import render_template
from app.routes.admin import admin


@admin.route('/')
def index():
    title = 'Admin'
    return render_template('admin/index.html',
                           title=title)
