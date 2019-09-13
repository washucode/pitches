from flask import Flask
from config import Config

app = Flask(__name__)

def  pitch_app():

    app.config.from_object(Config)

    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app