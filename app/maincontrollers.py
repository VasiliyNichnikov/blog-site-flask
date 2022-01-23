import datetime

from flask import g
from flask_login import current_user

from app import db
from app.profileuser.models import User
from manager import app
from manager import lm


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_request
def before_request() -> None:
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
