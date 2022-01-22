from flask_login import UserMixin

from app.database import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    # Никнейм пользователя
    nickname = db.Column(db.String(64), index=True, unique=True, nullable=False)
    # Email пользователя
    email = db.Column(db.String(120), index=True, unique=True, nullable=True)
    # Роль пользователя
    role = db.Column(db.SmallInteger(), default=ROLE_USER, nullable=False)
    # Иконка пользователя
    icon = db.Column(db.String(), nullable=True)
    # Информация о пользователе
    about_me = db.Column(db.String(500), nullable=True)

    # Все созданные блоги пользователя
    # blogs = db.relationship("Blog", backref="user")
    # Все написанные комментарии пользователя
    # comments = db.relationship("Comment", backref="user")

    # Метод __repr__ говорит Python как выводить объекты этого класса. Мы будем использовать его для отладки
    def __repr__(self) -> str:
        return f"<User-{self.nickname}>"

