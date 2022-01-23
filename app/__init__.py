from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Создание приложение
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

# Инициализация БД
db = SQLAlchemy(app)

# Подключение таблиц
from .blog import models
from .profileuser import models

# Создание БД
with app.test_request_context():
    db.create_all()

# Объекты для логирования пользователя
lm = LoginManager(app)
lm.login_view = "entity.login"

from . import views

# Настроен UploadSet
photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)
# patch_request_class(app)

# Подключение blueprints
import app.entity.controllers as entity
import app.profileuser.controllers as profileuser
import app.blog.controllers as blog

app.register_blueprint(entity.module)
app.register_blueprint(profileuser.module)
app.register_blueprint(blog.module)

# Логи
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
