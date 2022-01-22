from flask import Flask

from .database import db
from .general import models


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.general.controllers as firstmodule
    app.register_blueprint(firstmodule.module)

    return app
