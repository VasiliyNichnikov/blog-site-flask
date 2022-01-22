from flask import Flask

from app import create_app

app: Flask = create_app("config.DevelopmentConfig")

if __name__ == '__main__':
    app.run()
