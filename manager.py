from flask import Flask

from app import create_app, create_login_open_id, connecting_blueprints

app: Flask = create_app("config.DevelopmentConfig")
lm, open_id = create_login_open_id(app)
connecting_blueprints(app)

if __name__ == '__main__':
    app.run()
