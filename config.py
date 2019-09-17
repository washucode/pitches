class Config:
     DEBUG = True   
     SECRET_KEY = '435313ea80b5a872114356a1'
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://esther:p@localhost/pitches'
     UPLOADED_PHOTOS_DEST ='app/static/photos'