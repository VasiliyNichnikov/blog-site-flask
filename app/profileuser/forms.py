from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Length

from app.profileuser.models import User


class EditForm(FlaskForm):
    nickname = StringField("nickname", validators=[InputRequired()])
    about_me = TextAreaField("about_me", validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, **kwargs):
        super().__init__(**kwargs)
        self.__original_nickname = original_nickname

    def validate(self, extra_validators=None):
        if not FlaskForm.validate(self):
            return False
        if self.nickname.data == self.__original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user is not None:
            self.nickname.errors.append('Этот никнейм занят, попробуйте другой!')
            return False
        return True
