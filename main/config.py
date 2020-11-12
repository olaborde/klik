import os

class Config(object):
    SECREY_KY =  os.environ.get('SECRET_KEY') or "secret_string"