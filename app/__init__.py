from flask import Flask

from .database import db
from .entity import models


def create_app(selected_config: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(selected_config)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    import app.entity.controllers as firstmodule
    app.register_blueprint(firstmodule.module)

    return app
