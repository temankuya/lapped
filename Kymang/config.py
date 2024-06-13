#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7205564649:AAEAfz-BktDjIpm4xD5P8SjrtkRzIfoP4qw")
API_ID = int(os.environ.get("API_ID", "21037639"))
API_HASH = os.environ.get("API_HASH", "4793ebd12a1d545c668aa5e3aac11011")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://fredbot:fredbot@cluster0.oahrt9u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "21037639").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002198822633"))
BOT_ID = int(os.environ.get("BOT_ID", "7205564649"))

KITA = [int(x) for x in (os.environ.get("KITA", "21037639").split())]
