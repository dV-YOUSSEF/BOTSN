import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command([""])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/41a777f089288f7ad2571.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥](https://t.me/BPHEE)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/ELHYBA"), 
                    
                
                    InlineKeyboardButton(
                        "‹ الدعم ›", url=f"https://t.me/ZeSupport"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "‹ السورس ›", url=f"https://t.me/Source_Ze"),
                
        ],

            ]

        ),

    )

