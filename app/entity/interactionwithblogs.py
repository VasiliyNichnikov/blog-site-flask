from typing import List, Union

from app.blog.models import Blog
from app.profileuser.models import User


class BlogFilter:
    def __init__(self, nickname: str) -> None:
        self.__nickname = nickname

    def get_other_users_blogs(self) -> Union[List[Blog], None]:
        user = User.query.filter(User.nickname == self.__nickname).first()
        if user is not None:
            blogs = Blog.query.filter(Blog.user_id != user.id).all()
            result = []
            for item in blogs:
                if item.is_hide is False:
                    result.append(item)
            return result
        return None
