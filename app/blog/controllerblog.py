import os.path
from abc import ABC, abstractmethod
from io import BytesIO
from typing import Union, Any

from PIL import Image
from flask import url_for
from sqlalchemy import func
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app import db
from app.blog.models import Blog
from app.profileuser.models import User
from config import AVAILABLE_RESOLUTION_PREVIEW_BLOG

PATH_PHOTOS: str = "app/static/uploads"


class BlogParent(ABC):
    def __init__(self, title: str, description: str, file: Union[FileStorage, None]) -> None:
        self._title = title
        self._description = description
        self._file = file

    @abstractmethod
    def checking_correctness_of_parameters(self) -> bool:
        pass

    def check_existence_similar_block(self) -> bool:
        return Blog.query.filter(func.lower(Blog.title) == self._title.lower()).first() is not None

    @staticmethod
    def check_size_image(image: Image) -> bool:
        size = image.size
        return size == AVAILABLE_RESOLUTION_PREVIEW_BLOG

    def _save_image_on_server(self, image: Image) -> None:
        filename = secure_filename(self._file.filename)
        print(filename)
        image.save(f"{PATH_PHOTOS}/{filename}")

    @staticmethod
    def get_blog(nickname: str, title: str) -> Blog:
        user = User.query.filter(User.nickname == nickname).first()
        blog = Blog.query.filter(func.lower(Blog.title) == title and Blog.user_id == user.id).first()
        return blog

    def _get_image(self) -> Image:
        return Image.open(BytesIO(self._file.stream.read()))

    def _get_preview_url(self) -> str:
        return url_for("static", filename=f"uploads/{self._file.filename}")


class CreatorBlog(BlogParent):
    def __init__(self, title: str, description: str, file: Union[FileStorage, None]) -> None:
        super().__init__(title, description, file)
        self.__image: Image = self._get_image()

    @property
    def resolution_image(self) -> Union[Union[tuple[int, int], tuple], Any]:
        if self.__image is not None:
            return self.__image.size
        return tuple(0, 0)

    def checking_correctness_of_parameters(self) -> bool:
        block_exists = self.check_existence_similar_block()
        resolution_correct = self.check_size_image(self.__image)
        return block_exists is False and resolution_correct

    def add_blog_to_db(self, nickname: str) -> None:
        self._save_image_on_server(self.__image)
        user = User.query.filter(User.nickname == nickname).first()
        blog = self.__create_blog()
        user.blogs.append(blog)
        db.session.add(blog)
        db.session.commit()

    def __create_blog(self) -> Blog:
        preview_url = self._get_preview_url()
        return Blog(title=self._title, description=self._description, preview_url_image=preview_url)


class EditorBlog(BlogParent):
    __image = None

    def __init__(self, title: str, description: str, file: Union[FileStorage, None]) -> None:
        super().__init__(title, description, file)

    def checking_correctness_of_parameters(self) -> bool:
        block_exists = self.check_existence_similar_block()
        if self._file is None:
            return block_exists is False
        else:
            self.__image = self._get_image()
            resolution_correct = self.check_size_image(self.__image)
            return block_exists is False and resolution_correct

    def edit_blog_to_bd(self, nickname: str, title: str) -> None:
        blog = self.get_blog(nickname, title)
        blog.title = self._title
        blog.description = self._description
        if self._file is not None:
            if self.__image is None:
                self.__image = self._get_image()
            # self.__remove_old_image(blog.preview_url_image)
            preview_url = self._get_preview_url()
            blog.preview_url_image = preview_url
            self._save_image_on_server(self.__image)
        db.session.add(blog)
        db.session.commit()

    @staticmethod
    def __remove_old_image(filename):
        path_image = f"{PATH_PHOTOS}/{filename}"
        if os.path.isfile(path_image):
            os.remove(path_image)


class DestroyerBlog(BlogParent):
    def remove(self, nickname: str, title: str) -> None:
        blog = self.get_blog(nickname, title)
        if blog is not None:
            db.session.delete(blog)
            db.session.commit()

    def checking_correctness_of_parameters(self) -> bool:
        pass
