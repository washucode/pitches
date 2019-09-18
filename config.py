import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
     # DEBUG = True   
     DEBUG = False
     TESTING = False
     CSRF_ENABLED = True
     SECRET_KEY = '435313ea80b5a872114356a1'
     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
     
     UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
   


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}