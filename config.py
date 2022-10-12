import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

API_HASH = os.environ.get("API_HASH")
API_ID = int(os.environ.get("API_ID"))
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '5253097982').split()]
FORCE_SUB = os.environ.get("FORCE_SUB")
RemoveBG_API = os.environ.get('RemoveBG_API', 'HKAErRmcefuqK5DUUoFP9rWu')
