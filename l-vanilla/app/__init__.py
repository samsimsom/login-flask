

import os
from flask import Flask

from app.exts.database import db, session_interface


# application factory
def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ.get('APP_CONFIG'))
    app.session_interface = session_interface(db)

    db.init_app(app)

    # Blueprint registrations
    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.admin import admin
    app.register_blueprint(admin)

    from app.routes.user import user
    app.register_blueprint(user)

    return app


if __name__ == '__main__':
    create_app().run()
