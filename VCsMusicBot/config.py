import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCGbCm37hdIShjJijld6OoYa46KEHP4eDDYBSiQnQFY8Py-n4dpT9CzxCgdkEmdft2WNn6w5uY4m2otrO-TmAKsv-Gp3HwYE0gWqjX2RI1_tYlqBYIoJVFtdH2SK83n_x87Tw_sgd5up7XXjvxG0qbc6AdXm2FLwR4n2zBBriAR_H1hdNaftZEfTwPaRePcc30J-eMgsLNYTtgiI0CwjzNCN_aWLqmr7kNT1PU72kEitMOU66AXG9ghl-IXm_th34ZW_nSrQo62CCQ0q2psHksF01hGD_IYm-VWDgt4ePVxR8jpT65HKDhjQDQYzuBHWycukarUK8KSHIJRJHMdrnFuJQ0hQQA")
BOT_TOKEN = getenv("BOT_TOKEN","6094037167:AAEQ25oQVQB4QfRrmXYJ6m4eqfUywF08Mwo")
BOT_NAME = getenv("BOT_NAME","MuzGoBpt")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "uztrendmuz")
BG_IMAGE = getenv("BG_IMAGE", "https://graph.org/file/b52ff5f39ea5987284076.jpg")
admins = {621617473}
API_ID = int(getenv("API_ID", "534493"))
API_HASH = getenv("API_HASH","ac922823455e814e44020a9f3ee17914")
BOT_USERNAME = getenv("BOT_USERNAME","muzGoBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "muzGoBot")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "tanho_guruhh")
PROJECT_NAME = getenv("PROJECT_NAME", "muzGoBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/yozmela/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
