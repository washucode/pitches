import os
class Config:
     # DEBUG = True   
     SECRET_KEY = '435313ea80b5a872114356a1'
     SQLALCHEMY_DATABASE_URI = os.environ.get['DATABASE_URL']
     UPLOADED_PHOTOS_DEST ='app/static/photos'