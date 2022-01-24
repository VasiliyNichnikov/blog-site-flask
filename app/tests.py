import os
import unittest

from app.entity.logintoyandex import LoginToYandex
from app.entity.userdata import UserData
from app.profileuser.models import User
from app import app, db


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config.from_object("config.TestingConfig")
        self.app = app.test_client()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    # def test_avatar(self) -> None:
    #     u = User(nickname="Vasa", email="v@gmail.com")
    #     ly = LoginToYandex()
    #     access_token: str = "AQAAAAAeRGF2AAeg1TD2KY5HbUcbrqHbf254Qoc"
    #     ud: UserData = ly.get_user_data_test(access_token)
        # avatar =


if __name__ == '__main__':
    unittest.main()
