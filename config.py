import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "Z0deICTEIc|i}ypdv{0zWKL95"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    __base_dir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(__base_dir, "app.db")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

