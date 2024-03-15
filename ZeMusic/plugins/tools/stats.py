import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from ZeMusic.plugins.play.filters import command
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from ZeMusic import app
from ZeMusic.core.userbot import assistants
from ZeMusic.misc import SUDOERS, mongodb
from ZeMusic.plugins import ALL_MODULES
from ZeMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from ZeMusic.utils.decorators.language import language, languageCB
from ZeMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

app = Client("my_account", api_id, api_hash)

# Function to get statistics
def get_statistics():
    with app:
        all_chats = app.get_dialogs()
        group_count = 0
        user_count = 0
        group_links = []
        user_links = []

        for chat in all_chats:
            if chat.chat.type == "group" or chat.chat.type == "supergroup":
                group_count += 1
                group_links.append(f"{chat.chat.title}: t.me/{chat.chat.username}")
            elif chat.chat.type == "private":
                user_count += 1
                user_links.append(f"{chat.chat.first_name}: t.me/{chat.chat.username}")

        statistics = f"Total groups: {group_count}\nTotal users: {user_count}\n\nGroup links:\n"
        for link in group_links:
            statistics += link + "\n"
        statistics += "\nUser links:\n"
        for link in user_links:
            statistics += link + "\n"

        return statistics

# Command to fetch statistics
@app.on_message(filters.command("statistics", prefixes="/") & filters.me)
def fetch_statistics(_, message: Message):
    statistics = get_statistics()
    message.reply(statistics)

app.run()
