import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "28524972")) #optional
API_HASH = getenv("API_HASH", "409130d1d167a2c26862e65e8779a3d6") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "6334438071"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://ferdisyrl:buburayam1@cluster0.89myp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7856088201:AAE6kjerf0uAAl_8gkxH2V9um1AEa5SBRYg")
ALIVE_PIC = getenv("ALIVE_PIC", "https://envs.sh/PHS.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "✨halo gess!! Userbot aktif✨")
PM_LOGGER = getenv("PM_LOGGER"), or 0)
OPENAI_API = getenv("OPENAI_API", "")
RMBG_API = getenv("RMBG_API", "3RCCWg8tMBfDWdAs44YMfJmC")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "-1002456606377")
PM_LIMIT = int(getenv("PM_LIMIT") or 5)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/hitokizzy/Geez-Pyro")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ".")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGzQawATmQxqUy8QODS41yS8koHOIfWS0TDuMoDuLT0dIyazNKF8HmXoanLjXj3hd4Mk6Y97KN5TFgxSnCPkDrlTyntpGEL_aHHWwLtST2OxNcwAFj0a9U1WU1B01929NBdA5vg5mT4ruKK8e4gHViBXXZYpVBFUBzsePgfSm9X3l52capl1KYkP744r7k61Dn8uGM75GhPQJkrS7kpqg0cxlE2wVmM3plJBqw7QOy6WOYIGpq4HAVd6xGCc6Ai3TU7EaNGqhik6Q5vCDqQBxdpme7dXPWmg_VMNtOTDS4IEqu-IzXSe3IqW6nIGihnt4dA3xOlOQuruS020bbUvSLC0sSk3wAAAAF5j9q3AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")



