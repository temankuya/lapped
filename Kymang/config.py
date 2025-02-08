#Kymang

import os

from dotenv import load_dotenv

load_dotenv(".env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7413079332:AAEkWfEX95HXGefSg2s6fvVjR4iy3dGtHZg")
API_ID = int(os.environ.get("API_ID", "21037639"))
API_HASH = os.environ.get("API_HASH", "4793ebd12a1d545c668aa5e3aac11011")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://muhandrekurniawan:OUjBw8SpKs7hS8Vg@cluster0.q4rqd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ADMINS = [int(x) for x in (os.environ.get("ADMINS", "1755535456").split())]
MEMBER = [int(x) for x in (os.environ.get("MEMBER", "160").split())]
LOG_GRP = int(os.environ.get("LOG_GRP", "-1002498248720"))
BOT_ID = int(os.environ.get("BOT_ID", "7413079332"))

KITA = [int(x) for x in (os.environ.get("KITA", "1755535456").split())]
