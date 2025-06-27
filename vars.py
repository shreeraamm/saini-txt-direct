#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24410316"))
API_HASH = environ.get("API_HASH", "76c76a0c27fb01cbe6350399faf2c544")
BOT_TOKEN = environ.get("BOT_TOKEN", "6299804424:AAEfUTcsdTh1aMIojTyf36mphvQlTI8judQ")
OWNER = int(environ.get("OWNER", "516264904"))
CREDIT = "Ram"
AUTH_USER = os.environ.get('AUTH_USERS', '6135918896').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
