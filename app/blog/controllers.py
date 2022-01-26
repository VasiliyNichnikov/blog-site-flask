from typing import Union

from flask import Blueprint, Response, redirect, url_for, render_template, flash, request
from flask_login import login_required

from app.blog.controllerblog import CreatorBlog, EditorBlog
from app.blog.forms import BlogForm
from config import AVAILABLE_RESOLUTION_PREVIEW_BLOG

module = Blueprint("blog", __name__)


@module.route("/create_blog/<nickname>", methods=["GET", "POST"])
@login_required
def create_blog(nickname) -> Union[str, Response]:
    form = BlogForm()
    if form.validate_on_submit():
        file = request.files["photo"]
        if file.filename == '':
            flash("Изображение не загружено")
            return redirect(url_for("blog.create_blog", nickname=nickname))
        creator_blog: CreatorBlog = CreatorBlog(form.title.data, form.description.data, file)
        if creator_blog.checking_correctness_of_parameters():
            flash("Статья успешно создана")
            creator_blog.add_blog_to_db(nickname)
            return redirect(url_for("profileuser.user", nickname=nickname))
        elif creator_blog.check_existence_similar_block() is False:
            flash("Пост с таким именем уже есть, подумайте над новым названием")
        else:
            resolution = creator_blog.resolution_image
            flash(
                f"Превью загружено в неверном разрешение ({resolution[0]}x{resolution[1]}), "
                f"поддерживаемое разрешение: "
                f"({AVAILABLE_RESOLUTION_PREVIEW_BLOG[0]}x{AVAILABLE_RESOLUTION_PREVIEW_BLOG[1]})")
        return redirect(url_for("blog.create_blog", nickname=nickname))
    return render_template("blog/creating-blog.html", form=form, name_post="Новый блог",
                           name_submit_button="Опубликовать блог", url_image=None)


@module.route("/edit_blog/<nickname>/<title>", methods=["GET", "POST"])
@login_required
def edit_blog(nickname: str, title: str) -> Union[str, Response]:
    form = BlogForm()
    url_image = None
    if form.validate_on_submit():
        file = request.files["photo"]
        if file.filename == '':
            file = None
        editor_blog: EditorBlog = EditorBlog(form.title.data, form.description.data, file)
        if editor_blog.checking_correctness_of_parameters():
            flash("Статья успешно изменена")
            editor_blog.edit_blog_to_bd(nickname, title)
            return redirect(url_for("profileuser.user", nickname=nickname))
        else:
            flash("Проблема с выбранным изображением или такой пост уже существует.")
    else:
        blog = EditorBlog.get_blog(nickname, title)
        if blog is not None:
            form.title.data = blog.title
            form.description.data = blog.description
            url_image = blog.preview_url_image
        else:
            pass  # TODO Ошибка должна быть
    return render_template("blog/creating-blog.html", form=form, name_post="Редактирование блога",
                           name_submit_button="Сохранить изменения", url_image=url_image)


@module.route("/hide_blog/<nickname>/<title>")
@login_required
def hide_blog(nickname: str, title: str) -> Union[str, Response]:
    return f"Скрыть блог: {nickname}, {title}"


@module.route("/remove_blog/<nickname>/<title>")
@login_required
def remove_blog(nickname: str, title: str) -> Union[str, Response]:
    return f"Удалить блог: {nickname}, {title}"
