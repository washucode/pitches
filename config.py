import os

class Config(object):
     # DEBUG = True   
     DEBUG = False
     TESTING = False
     CSRF_ENABLED = True
     SECRET_KEY = '435313ea80b5a872114356a1'
     
     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://esther:p@localhost/pitches'
     UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get['DATABASE_URL']


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}