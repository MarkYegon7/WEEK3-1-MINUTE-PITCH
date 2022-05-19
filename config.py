import os
from distutils.debug import DEBUG


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
    pass

class TestConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}