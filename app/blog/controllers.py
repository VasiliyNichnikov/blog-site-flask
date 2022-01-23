# import os.path
from typing import Union

from flask import Blueprint, Response, redirect, url_for, render_template, request, flash
from flask_login import login_required
# from werkzeug.utils import secure_filename

# from app import app
from app.blog.forms import BlogForm

module = Blueprint("blog", __name__)
ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]


@module.route("/create_blog", methods=["GET", "POST"])
@login_required
def create_blog() -> Union[str, Response]:
    form = BlogForm()
    if form.validate_on_submit():
        flash("Статья успешно создана")
        print(form.photo.data)
        return redirect(url_for("entity.index"))
    else:
        pass
    return render_template("blog/creating-blog.html", form=form)


# @module.route("/upload_image_to_blog", methods=["GET", "POST"])
# def upload_image_to_blog() -> Union[str, Response]:
#     if request.method == "POST":
#         if "file" not in request.files:
#             flash("Unreadable file")
#         file = request.files["file"]
#         if file.filename == '':
#             flash("File not found")
#             return redirect(url_for("blog.create_blog"))
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config.UPLOAD_FOLDER, filename))
#             return redirect(url_for("/upload_image_to_blog"))
#     return redirect(url_for("blog.create_blog"))


# def allowed_file(filename: str) -> bool:
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
