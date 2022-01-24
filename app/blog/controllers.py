from typing import Union

from flask import Blueprint, Response, redirect, url_for, render_template, flash, request
from flask_login import login_required

from app.blog.creatorblog import CreatorBlog
from app.blog.forms import BlogForm
from config import AVAILABLE_RESOLUTION_PREVIEW_BLOG

module = Blueprint("blog", __name__)


@module.route("/create_blog/<nickname>", methods=["GET", "POST"])
@login_required
def create_blog(nickname) -> Union[str, Response]:
    form = BlogForm()
    if form.validate_on_submit():
        file = request.files["photo"]
        cb: CreatorBlog = CreatorBlog(form.title.data, form.description.data, file)
        block_exists: bool = cb.check_existence_similar_block()
        resolution_correct: bool = cb.check_size_photo()
        if resolution_correct is True and block_exists is False:
            flash("Статья успешно создана")
            cb.save_image_on_server()
            cb.add_block_to_db(nickname)
            return redirect(url_for("entity.index"))
        elif block_exists is False:
            flash("Пост с таким именем уже есть, подумайте над новым названием")
        else:
            resolution = cb.resolution_image
            flash(
                f"Превью загружено в неверном разрешение ({resolution[0]}x{resolution[1]}), "
                f"поддерживаемое разрешение: "
                f"({AVAILABLE_RESOLUTION_PREVIEW_BLOG[0]}x{AVAILABLE_RESOLUTION_PREVIEW_BLOG[1]})")
        return redirect(url_for("blog.create_blog", nickname=nickname))
    else:
        pass
    return render_template("blog/creating-blog.html", form=form)
