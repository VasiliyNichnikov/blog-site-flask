from app import *

app: Flask = create_app("config.DevelopmentConfig")
lm, open_id = create_login_open_id(app)
connecting_blueprints(app)
logs(app)
from app import maincontrollers

if __name__ == '__main__':
    app.run()
