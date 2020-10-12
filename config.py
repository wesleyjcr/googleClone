class Config(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
    SECRET_KEY = 'pK4I,B2@OLt;#/*yzQzskz<g8-O8u6]CnkC]k{i0MT^m;z!PdC?5!38@ak)&zJj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass



