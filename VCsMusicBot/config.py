import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "uztrendmuz")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/b52ff5f39ea5987284076.jpg")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MuzGoBot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "tanho_guruhh")
PROJECT_NAME = getenv("PROJECT_NAME", "MuzGoBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/yozmela/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
