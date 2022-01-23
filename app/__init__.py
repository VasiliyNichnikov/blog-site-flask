import os.path

from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID

from config import base_dir
from .blog import models
from .database import db
from .profileuser import models


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
    import app.profileuser.controllers as profileuser
    app.register_blueprint(entity.module)
    app.register_blueprint(profileuser.module)


def logs(app: Flask) -> None:
    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler("tmp/myblog.log", 'a', 1 * 1024 * 1024, 10)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info("MyBlog startup")
