"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import random
from Geez import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = OWNER_ID
    message = "saya ingin bertanya kak"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

geezlogo = [
    "https://envs.sh/PHS.jpg",
    "https://envs.sh/0a0.jpg",
    "https://envs.sh/0aW.jpg",
    "https://envs.sh/Pvl.jpg"
]

alive_logo = random.choice(geezlogo)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "✨Halo!, Saya Asisstant Userbot Ferdi"
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/BestieVirtual"),
            InlineKeyboardButton("Owner", url="https://t.me/fsyrl"),
            InlineKeyboardButton("Store", url="https://t.me/Galerisyrl"),        
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
