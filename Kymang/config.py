#Kymang

import os
from dotenv import load_dotenv

load_dotenv(".env")

def get_env_int(key, default="0"):
    try:
        return int(os.environ.get(key, default))
    except ValueError:
        return 0

def get_env_list(key, default=""):
    return [int(x) for x in os.environ.get(key, default).split() if x.isdigit()]

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = get_env_int("API_ID", "0")
API_HASH = os.environ.get("API_HASH", "")
MONGO_URL = os.environ.get("MONGO_URL", "")
ADMINS = get_env_list("ADMINS", "1755535456")
MEMBER = get_env_list("MEMBER", "160")
LOG_GRP = get_env_int("LOG_GRP", "-1001234567890")
BOT_ID = get_env_int("BOT_ID", "7413079332")
KITA = get_env_list("KITA", "1755535456")
