import os.path

from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID

from config import base_dir
from .database import db
from .entity import models


def create_app(selected_config: str) -> Flask:
    # Создание приложения Flask
    app = Flask(__name__)
    app.config.from_object(selected_config)

    # Инициализация БД
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
    return app


def create_login_open_id(app: Flask) -> (LoginManager, OpenID):
    lm = LoginManager()
    lm.init_app(app)
    lm.login_view = "entity.login"
    open_id = OpenID(app, os.path.join(base_dir, "tmp"))
    return lm, open_id


def connecting_blueprints(app: Flask) -> None:
    import app.entity.controllers as entity
    app.register_blueprint(entity.module)
