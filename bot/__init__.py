import logging
import os
import sys
import time
from logging import basicConfig
from logging import DEBUG
from logging import getLogger
from logging import INFO

from telethon import TelegramClient
from telethon.sessions import StringSession

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
ENV = bool(os.environ.get("ENV", True)

if ENV:
    LOGGER = True

    BOT_NAME = os.environ.get("BOT_NAME", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    anjana = TelegramClient(None, APP_KEY, API_HASH)

    LOGS = getLogger(__name__)

else:
    sys.exit(1)
