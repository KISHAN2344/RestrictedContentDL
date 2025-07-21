# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

from os import getenv
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env")
except:
    pass

    if not getenv("BOT_TOKEN") or not getenv("BOT_TOKEN").count(":") == 1:
        print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
        exit(1)

    if (
        not getenv("SESSION_STRING")
        or getenv("SESSION_STRING") == "xxxxxxxxxxxxxxxxxxxxxxx"
    ):
        print("Error: SESSION_STRING must be set with a valid string")
        exit(1)


# Pyrogram setup
class PyroConf(object):
    API_ID = int(getenv("API_ID", "20386593"))
    API_HASH = getenv("API_HASH", "51970327f8e01b3409a3102d86f5c3ac")
    BOT_TOKEN = getenv("BOT_TOKEN", "8135705187:AAFGcx40XIaQFaEZgLSRUbwo46SPnUEGEzA")
    SESSION_STRING = getenv("SESSION_STRING")
    BOT_START_TIME = time()
