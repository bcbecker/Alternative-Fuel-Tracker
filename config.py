import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "SECRET_KEY does not exist")
    API_KEY = os.environ.get('API_KEY', "API_KEY does not exist")