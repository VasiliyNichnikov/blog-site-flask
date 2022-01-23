from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Length


class EditForm(FlaskForm):
    nickname = StringField("nickname", validators=[InputRequired()])
    about_me = StringField("about_me", validators=[Length(min=0, max=140)])
