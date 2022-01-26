from urllib.parse import urlencode

from flask import request
from requests import post, get

from .userdata import UserData


class LoginToYandex:
    __client_id = "7fbc27b38cbd4e5bb14fa7c3b6ce40b2"
    __client_secret = "670b1eb86f56490b93b1ff912b9149bc"
    __base_url = "https://oauth.yandex.ru/"
    __base_url_test = "https://oauth.yandex.ru/authorize?response_type=token&client_id={}"
    __token_url = "https://login.yandex.ru/info?format=json&oauth_token={}"

    def get_user_data(self) -> UserData:
        access_token = self.__get_access_token(self.__base_url)
        user_data = get(self.__token_url.format(access_token)).json()
        return UserData(user_data["login"],
                        user_data["first_name"],
                        user_data["last_name"],
                        user_data["default_email"],
                        user_data["is_avatar_empty"],
                        user_data["default_avatar_id"])

    def get_access_url(self) -> str:
        return self.__base_url + f"authorize?response_type=code&client_id={self.__client_id}"

    def __get_access_token(self, url: str) -> str:
        data = {
            'grant_type': 'authorization_code',
            'code': request.args.get('code'),
            'client_id': self.__client_id,
            'client_secret': self.__client_secret
        }
        data = urlencode(data)
        info = post(url + "token", data).json()
        return info["access_token"]
