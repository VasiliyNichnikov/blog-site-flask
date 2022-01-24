import datetime

from app import db


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer(), primary_key=True)
    # Превью стаьи (ссылка на изображение)
    preview_image_file = db.Column(db.String(), index=True, nullable=False)
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
    # Время создания комментария
    created_on = db.Column(db.DateTime(), default=datetime.datetime.utcnow(), nullable=False)

    def __repr__(self) -> str:
        return f"<Comment {self.description}>"
