from typing import Union

from flask import Blueprint
from flask import render_template, flash, redirect, Response

from app.entity.forms import LoginForm

module = Blueprint("entity", __name__)

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"}
]


@module.route('/')
@module.route('/index')
def index() -> str:
    user = {"nickname": "Vasiliy"}
    posts = [
        {
            "author": {"nickname": "Artem"},
            "body": "Интересный пост из мира животных!"
        },
        {
            "author": {"nickname": "Matvey"},
            "body": "Как узнать человека по одежде?"
        }
    ]
    return render_template("main.html",
                           user=user,
                           posts=posts)


@module.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for OpenId = {form.open_id.data}; Remember me = {str(form.remember_me.data)}")
        return redirect("/index")
    return render_template("entity/login.html", title="Sign In", form=form, providers=OPENID_PROVIDERS)
