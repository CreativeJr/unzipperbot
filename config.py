# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("APP_ID", "4926633"))
    API_HASH = os.environ.get("API_HASH", "be7b1d39ac5116d22701f8b6ac956785")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5886778677:AAG_iE9Qy20ixIHJ_lbqVu6mp4aVPwLji2k")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001887884003"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1359955110"))
    MONGODB_URL = os.environ.get("MONGODB_URL", "mongodb+srv://unzipper:unzipper@cluster0.fc8uopr.mongodb.net/?retryWrites=true&w=majority")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN", "jutJvhzwR9dq7VhLa7tBdYPySUKJihkU")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
