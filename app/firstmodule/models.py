import datetime

from app.database import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    # Никнейм пользователя
    nickname = db.Column(db.String(64), index=True, unique=True, nullable=False)
    # Email пользователя
    email = db.Column(db.String(120), index=True, unique=True, nullable=True)
    # Пароль пользователя в зашифрованном виде
    password = db.Column(db.String(50), index=True, nullable=False)
    # Роль пользователя
    role = db.Column(db.SmallInteger(), default=ROLE_USER, nullable=False)
    # Иконка пользователя
    icon = db.Column(db.String(), nullable=False)
    # Информация о пользователе
    about_me = db.Column(db.String(500), nullable=True)
    # Все созданные блоги пользователя
    blogs = db.relationship("Blog", backref="user")
    # Все написанные комментарии пользователя
    comments = db.relationship("Comment", backref="user")

    # Метод __repr__ говорит Python как выводить объекты этого класса. Мы будем использовать его для отладки
    def __repr__(self) -> str:
        return f"<User {self.nickname}>"


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer(), primary_key=True)
    # Название статьи
    title = db.Column(db.String(120), index=True, unique=True, nullable=False)
    # Описание статьи
    description = db.Column(db.String(), nullable=False)
    # Кол-во лайков на статье
    quantity_likes = db.Column(db.Integer(), default=0, index=True, nullable=False)
    # Время создания статьи
    created_on = db.Column(db.DateTime(), default=datetime.datetime.utcnow(), nullable=False)
    # Id пользователя, кому данная статья принадлежит
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    # Все написанные комментарии под статьей
    comments = db.relationship("Comment", backref="blog")

    def __repr__(self) -> str:
        return f"<Blog {self.title}>"


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer(), primary_key=True)
    # Описание комментария
    description = db.Column(db.String(200), nullable=False)
    # Id пользователя, кому данный комментарий принадлежит
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    # Id блога, под которым написан комментарий
    comment_id = db.Column(db.Integer(), db.ForeignKey("blogs.id"))

    def __repr__(self) -> str:
        return f"<Comment {self.description}>"