import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "Z0deICTEIc|i}ypdv{0zWKL95"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = "app/static/img"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "app.db")


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "test.db")
