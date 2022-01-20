import os

base_dir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base_dir, "app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(base_dir, "db_repository")


CSRF_ENABLED: bool = True
SECRET_KEY: str = "Z0deICTEIc|i}ypdv{0zWKL95"

OPENID_PROVIDERS = [
    {"name": "Google", "url": "https://www.google.com/accounts/o8/id"}
]