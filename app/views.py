from typing import Union

from flask import render_template, flash, redirect, Response

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
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
    return render_template("index.html",
                           user=user,
                           posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login() -> Union[str, Response]:
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for OpenId = {form.open_id.data}; Remember me = {str(form.remember_me.data)}")
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form, providers=app.config["OPENID_PROVIDERS"])
