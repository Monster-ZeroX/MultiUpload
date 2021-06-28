# (c) Copyright 21-22 lucifeermorningstar@GitHub, < https://GitHub.com/lucifeermorningstar >
# written By Devil


from telethon import TelegramClient
from config import *
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


anjana = TelegramClient('anjana', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 
