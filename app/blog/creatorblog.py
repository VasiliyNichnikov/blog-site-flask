from io import BytesIO
from typing import Tuple

from PIL import Image
from flask import url_for
from sqlalchemy import func
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app import db
from app.blog.models import Blog
from app.profileuser.models import User
from config import AVAILABLE_RESOLUTION_PREVIEW_BLOG


class CreatorBlog:
    __path_photos = "app/static/uploads"

    def __init__(self, title: str, description: str, file: FileStorage) -> None:
        self.__title = title
        self.__description = description
        self.__file = file
        self.__image = None
        self.__filename = None

    @property
    def resolution_image(self) -> Tuple[int]:
        if self.__image is not None:
            return self.__image.size
        return tuple(0, 0)

    def check_size_photo(self) -> bool:
        self.__image = self.__get_image()
        size = self.__image.size
        return size == AVAILABLE_RESOLUTION_PREVIEW_BLOG

    def check_existence_similar_block(self) -> bool:
        return Blog.query.filter(func.lower(Blog.title) == self.__title.lower()).first() is not None

    def save_image_on_server(self) -> None:
        if self.__image is None:
            self.__image = self.__get_image()
        self.__filename = secure_filename(self.__file.filename)
        self.__image.save(f"{self.__path_photos}/{self.__filename}")

    def add_block_to_db(self, nickname: str) -> None:
        user = User.query.filter(User.nickname == nickname).first()
        blog = self.__create_blog()
        user.blogs.append(blog)
        db.session.add(blog)
        db.session.commit()

    def __create_blog(self) -> Blog:
        preview_url = url_for("static", filename=f"uploads/{self.__filename}")
        return Blog(title=self.__title, description=self.__description, preview_url_image=preview_url)

    def __get_image(self) -> Image:
        return Image.open(BytesIO(self.__file.stream.read()))
