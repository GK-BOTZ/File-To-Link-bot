# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '17108931'))
    API_HASH = str(getenv('API_HASH', '436b24700208cae55ded351d8f25fd7a'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6998955142:AAHRLB4BfFMKf1x8SW-gd2IoS3GShkWhHTA'))
    name = str(getenv('name', 'KRS_File_To_BoT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002113631575'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5300197778").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Kushi_Yarige_bedda'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://krsfiletolinkbot-39fb9a40c0d9.herokuapp.com/".format(FQDN)
    else:
        URL = "https://krsfiletolinkbot-39fb9a40c0d9.herokuapp.com/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://adminleech:UHee459K12WJBfDY@cluster0.xsmgkhi.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'KRS_BOTS'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002012506663")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'onepagelink.in')
    SHORTLINK_API = getenv('SHORTLINK_API', 'c47e1c4469c0a66e74af7153cb8f4d3b304d010')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/rk_back_up/18')
