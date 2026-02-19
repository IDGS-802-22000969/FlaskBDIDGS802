from re import DEBUG


class config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False

 class DevelopmentConfig(config):   
    DEBUG= True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://localhost:3306:root/idgs802'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
