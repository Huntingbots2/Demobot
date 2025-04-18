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

     # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
