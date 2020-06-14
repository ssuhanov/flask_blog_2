class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:passroot@localhost/test1'
    SECRET_KEY = 'Something_vEry_seCret_herE'
