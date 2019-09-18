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

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True