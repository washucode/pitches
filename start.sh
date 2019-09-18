export SECRET_KEY=435313ea80b5a872114356a1
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL='postgresql+psycopg2://esther:p@localhost/pitches'
python3 manage.py db upgrade