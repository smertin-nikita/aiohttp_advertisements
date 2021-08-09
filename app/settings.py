import asyncio
import os
import pathlib
import sys

from dotenv import load_dotenv

if sys.version_info >= (3, 8) and sys.platform.lower().startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

BASE_DIR = pathlib.Path(__file__).parent.parent


config_path = os.path.join(BASE_DIR, 'config', '.env')
if os.path.exists(config_path):
    load_dotenv(config_path)

config = {
    'postgres': {
        'database': os.getenv('PGDATABASE'),
        'user': os.getenv('PGUSER'),
        'password': os.getenv('PGPASSWORD'),
        'host': os.getenv('PGHOST'),
        'port': os.getenv('PGPORT'),
    }
}

