from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    open_id = StringField("open_id", validators=[InputRequired()])
    remember_me = BooleanField("remember_me", default=False)
