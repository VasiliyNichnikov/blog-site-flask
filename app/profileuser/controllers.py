from typing import Union

from flask import Blueprint, Response, flash, redirect, url_for, render_template, g
from flask_login import login_required

from app import db
from app.profileuser.forms import EditForm
from app.profileuser.models import User

module = Blueprint("profileuser", __name__)


@module.route("/user/<nickname>")
@login_required
def user(nickname) -> Union[str, Response]:
    user = User.query.filter(User.nickname == nickname).first()
    if user is None:
        flash(f"User {nickname} not found.")
        return redirect(url_for("entity.index"))
    posts = [
        {
            "author": user,
            "body": "Интересный пост из мира животных!"
        },
        {
            "author": user,
            "body": "Как узнать человека по одежде?"
        },
        {
            "author": user,
            "body": "Когда мы станем есть больше, а весить меньше?"
        }
    ]
    return render_template("profileuser/user.html", user=user, posts=posts)


@module.route("/edit", methods=["GET", "POST"])
@login_required
def edit() -> Union[str, Response]:
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("profileuser.edit"))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template("profileuser/edit.html", form=form)
