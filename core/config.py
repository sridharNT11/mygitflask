class Config(object):
    DEBUG = False
    TESTING = False
    
class ProductionConfig(Config):
    DATABASE_URI = 'mysql+mysqldb://numerote_vrsi_member:QX-BZBwlKWEg@68.66.226.118/numerote_vrsi_member' # live db # live db (wacem21 database)
    
    DEBUG = True
    CACHE_TYPE  = 'NULL'
    UPLOAD_PATH  = 'images'
    SESSION_TYPE = 'filesystem'
    TIMEZONE     = 'Asia/Calcutta'
    # JSONIFY_PRETTYPRINT_REGULAR = False

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_GUN_KEY = 'DEVKEY23'

class SECRET_KEY(Config):
    SECRET_KEY = '5678906567890543346789976565'

