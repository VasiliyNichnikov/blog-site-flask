from io import BytesIO
from typing import Union

from PIL import Image
from flask import Blueprint, Response, redirect, url_for, render_template, flash, request
from flask_login import login_required

from app import photos, db
from app.blog.forms import BlogForm
from app.blog.models import Blog
from sqlalchemy import func
from config import AVAILABLE_RESOLUTION_PREVIEW_BLOG

module = Blueprint("blog", __name__)


@module.route("/create_blog", methods=["GET", "POST"])
@login_required
def create_blog() -> Union[str, Response]:
    form = BlogForm()
    if form.validate_on_submit():
        file = request.files["photo"]
        image = Image.open(BytesIO(file.stream.read()))
        size = image.size
        blog = Blog.query.filter(func.lower(Blog.title) == form.title.data.lower()).first()
        if size == AVAILABLE_RESOLUTION_PREVIEW_BLOG and blog is None:
            flash("Статья успешно создана")
            filename = photos.save(form.photo.data)
            blog = Blog(title=form.title.data, description=form.description.data, preview_image_file=filename)
            db.session.add(blog)
            db.session.commit()
            return redirect(url_for("entity.index"))
        elif blog is not None:
            flash("Пост с таким именем уже есть, подумайте над новым названием")
        else:
            flash(
                f"Превью загружено в неверном разрешение ({size[0]}x{size[1]}), "
                f"поддерживаемое разрешение: "
                f"({AVAILABLE_RESOLUTION_PREVIEW_BLOG[0]}x{AVAILABLE_RESOLUTION_PREVIEW_BLOG[1]})")
        return redirect(url_for("blog.create_blog"))
    else:
        pass
    return render_template("blog/creating-blog.html", form=form)
