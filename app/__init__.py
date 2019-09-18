from flask import Flask
from config import Config

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES



app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def  pitch_app():

    # app.config.from_object(Config)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # initialize extensions
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

     # configure UploadSet
    configure_uploads(app,photos)
    # registering main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    # registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app