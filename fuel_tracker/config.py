import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "SECRET_KEY does not exist")
    NREL_API_KEY = os.environ.get('NREL_API_KEY', "API_KEY does not exist")
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', "API_KEY does not exist")
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False

class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    TESTING = True