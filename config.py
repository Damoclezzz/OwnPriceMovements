import os
from dotenv import load_dotenv

load_dotenv()

LEADING_PAIR = os.getenv('LEADING_PAIR')
DRIVEN_PAIR = os.getenv('DRIVEN_PAIR')
