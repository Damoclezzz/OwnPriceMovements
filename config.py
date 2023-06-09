import os
from dotenv import load_dotenv

load_dotenv()

LEADING_PAIR = os.getenv('LEADING_PAIR')
DRIVEN_PAIR = os.getenv('DRIVEN_PAIR')

BINANCE_PUBLIC_BASE_URL = os.getenv('BINANCE_PUBLIC_BASE_URL')