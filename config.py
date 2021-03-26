import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://charity:21193@localhost/pitches'
     

class ProdConfig(Config):

    pass


class DevConfig(Config):
    
    DEBUG = True

#Dictionary for configurations
config_options = {
'development':DevConfig,
'production':ProdConfig
} 