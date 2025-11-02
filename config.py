import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv('7206142113:AAHAVWbMifD51rU89K-BBZ9HSgMJnNXboyo')
    MANAGER_CHAT_ID = os.getenv('MANAGER_CHAT_ID')
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///bot_database.db')

config = Config()