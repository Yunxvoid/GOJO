# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

from GOJO.vars import HEROKU_API_KEY, HEROKU_APP_NAME, REDIS_URL

def get_user_list(config, key):
    with open("{}/Senku/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    BOT_TOKEN = "BOT_TOKEN"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5001899507  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Yun윤"
    SUPPORT_CHAT = "gojo_support"  # Your own group for support, do not add the @
    LOG_CHANNEL = (
       -1001668540922
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "something://somewhat:user@hosturl:port/databasename"  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

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
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
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
    ERROR_LOG_CHANNEL = -1001668540922  # needed to make sure 'save from' messages persist
    HEROKU_API_KEY = 5001899507  # Your Heroku API key, get it from 'https://dashboard.heroku.com/account
    HEROKU_APP_NAME = (
        "awoo"  # Enter the Heroku app name here (Must an exact same name with your input above)
    )
    ARQ_API = "awoo"
    APOD_API_KEY = "awoo"
    REDIS_URL = "awoo"
    ANIME_NAME = "Jujutsu kaisen"
    START_MEDIA = "https://telegra.ph/file/f2d390bad48ee15c36011.mp4"
    BOT_USERNAME = "Gojoa_satoru_bot"
    UPDATE_CHANNEL = "gojo_bot_updates"
    ALIVE_MEDIA = "https://telegra.ph/file/a6c30cd075df16dae7bb5.mp4"
    BOT_ID = 5484116052
    STATS_IMG = "awoo"
    NETWORK_USERNAME = "VoidxNetwork"
    NETWORK = "【V๏ɪ፝֟𝔡】»Network«"
    INLINE_IMG = "https://telegra.ph/file/1f5aa2587aace405edca8.jpg"
    API_WEATHER = "awoo"
    OWNER_WELCOME_MEDIA = ""

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True