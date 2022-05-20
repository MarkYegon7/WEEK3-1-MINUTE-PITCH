import os



class Config:
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:mark@localhost/pitches'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mark:Wildwave123@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '12345'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://tiyjvwwjszqgjb:d3bbe2d58bd0931ca625e93aea9f75d25240d282bc0cc606c5d8bab1d5d9649d@ec2-3-230-122-20.compute-1.amazonaws.com:5432/d3353t1ahfhs8j'
    

class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}