class Config(object):
    LOGGER = True
    API_ID = 3975570
    API_HASH = "680b62f2844aa1954216f6cb99d2f3d9"
    TOKEN = "1746875218:AAFPvcA5kZhCi-TOxAE6j6wKL9BErVOrXsM"  
    OWNER_ID= 1606221784
    
    SUPPORT_CHAT = "AsunaRobotSupport" 
    START_IMG = ""
    EVENT_LOGS = -1001432768300
    MONGO_DB_URI= "mongodb+srv://ghost:ghost123@hunter.z1x1x.mongodb.net/?retryWrites=true&w=majority&appName=Hunter"
   
    DATABASE_URL = "postgresql://tghbot_owner:npg_jae9mlh4kOMN@ep-shy-feather-a4hofch2-pooler.us-east-1.aws.neon.tech/tghbot?sslmode=require"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
