import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "Z0deICTEIc|i}ypdv{0zWKL95"

    # SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    __base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(__base_dir, "app.db")


class ProductionConfig(Config):
    DEBUG = False


# base_dir = os.path.abspath(os.path.dirname(__file__))
# print(os.path.join(base_dir, "app.db"))


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


# SQLALCHEMY_MIGRATE_REPO = os.path.join(base_dir, "db_repository")

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"}
]
