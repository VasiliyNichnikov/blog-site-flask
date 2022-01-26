from typing import Union

from flask import Blueprint, Response, flash, redirect, url_for, render_template, g
from flask_login import login_required

from app import db
from app.profileuser.forms import EditForm
from app.profileuser.models import User
from app.blog.models import Blog

module = Blueprint("profileuser", __name__)


@module.route("/user/<nickname>")
@login_required
def user(nickname) -> Union[str, Response]:
    user = User.query.filter(User.nickname == nickname).first()
    if user is None:
        flash(f"Пользователь {nickname} не найден")
        return redirect(url_for("entity.index"))
    blogs = Blog.query.filter(Blog.user_id == user.id).all()
    return render_template("profileuser/user.html", user=user, blogs=blogs)


@module.route("/edit", methods=["GET", "POST"])
@login_required
def edit() -> Union[str, Response]:
    form = EditForm()
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash("Изменения были сохранены")
        return redirect(url_for("profileuser.edit"))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template("profileuser/edit.html", form=form)
