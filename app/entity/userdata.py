from typing import Union


class UserData:
    def __init__(self, login: str, first_name: str, last_name: str, email: str,
                 is_avatar_empty: bool, avatar_id: Union[None, str] = None) -> None:
        self.__login = login
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__is_avatar_empty = is_avatar_empty
        self.__avatar_id = avatar_id

    @property
    def login(self) -> str:
        return self.__login

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def avatar_id(self) -> Union[None, str]:
        if self.__is_avatar_empty:
            return "0"
        return self.__avatar_id
