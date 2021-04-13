

from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin')


def load_routes():
    from app.routes.admin import routes


load_routes()
