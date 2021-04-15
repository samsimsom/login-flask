

import os
from flask import Flask

from app.exts.database import db
from app.exts.csrf import csrf


# application factory
def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_CONFIG'))

    db.init_app(app)
    csrf.init_app(app)

    # Blueprint registrations
    from app.cli import app_cli, user_cli
    app.register_blueprint(app_cli)
    app.register_blueprint(user_cli)

    from app.routes.main import main
    app.register_blueprint(main)
    # csrf.exempt(admin_category)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.admin import admin
    app.register_blueprint(admin)

    from app.routes.user import user
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    create_app().run()
