from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","21134445"))
API_HASH = getenv("API_HASH","231c18ea7273824491d6bf05425ab74e")

BOT_TOKEN = getenv("8018252288:AAE36WZAP1ajjheZRtYk2zU4OeMoxXonhf4")
OWNER_ID = int(getenv("OWNER_ID","8156708830"))

MONGO_DB_URI = getenv("mongodb+srv://dragonbytexbotz:ZYivvnFytzvM9b5l@cluster0.w4qnbpw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","https://t.me/ThronexCodex")
