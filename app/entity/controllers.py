from typing import Union

from flask import Blueprint, g, url_for, request
from flask import render_template, redirect, Response
from flask_login import login_required, login_user, logout_user

from app import db
from app.profileuser.models import User, ROLE_USER
# from manager import lm
from .logintoyandex import LoginToYandex
from .userdata import UserData

module = Blueprint("entity", __name__)


# @lm.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


@module.route("/get_yandex_token")
def get_yandex_token() -> Union[str, Response]:
    if g.user.is_authenticated:
        return redirect(url_for("entity.index"))

    ly = LoginToYandex()
    if request.args.get('code', False):
        ud: UserData = ly.get_user_data()
        user = User.query.filter(User.email == ud.email).first()
        if user is None:
            nickname = ud.first_name
            user = User(nickname=nickname, email=ud.email, role=ROLE_USER, avatar_id=ud.avatar_id)
            db.session.add(user)
            db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("entity.index"))
    else:
        access_url = ly.get_access_url()
        return redirect(access_url)


@module.route('/')
@module.route('/index')
@login_required
def index() -> str:
    user = g.user.nickname
    posts = [
        {
            "author": {"nickname": "Артем"},
            "body": "Интересный пост из мира животных!"
        },
        {
            "author": {"nickname": "Матвей"},
            "body": "Как узнать человека по одежде?"
        },
        {
            "author": {"nickname": "Богдан"},
            "body": "Когда мы станем есть больше, а весить меньше?"
        }
    ]
    return render_template("main.html",
                           user=user,
                           posts=posts)


# @module.before_request
# def before_request() -> None:
#     g.user = current_user


@module.route("/login")
def login() -> Union[str, Response]:
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for("index"))
    return render_template("entity/yandex-login.html")


@module.route("/logout")
def logout() -> Response:
    logout_user()
    return redirect(url_for("entity.index"))
