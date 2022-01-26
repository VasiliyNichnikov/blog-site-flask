from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from app import photos
from wtforms.validators import InputRequired, Length


class BlogForm(FlaskForm):
    title = StringField("title", validators=[InputRequired()])
    photo = FileField(validators=[FileAllowed(photos, "Image only!")])
    description = TextAreaField("description", validators=[InputRequired(), Length(min=0, max=10000)])