import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charity:21193@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos' 

class ProdConfig(Config):

    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charity:21193@localhost/pitches_test'



class DevConfig(Config):
    
    DEBUG = True

#Dictionary for configurations
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 