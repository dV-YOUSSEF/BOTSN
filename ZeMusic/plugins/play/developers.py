import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["يوسف","المبرمج يوسف","مبرمج السورس","مبرمج"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/28c072a310a6ffe042c84.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗬.𝗢.𝗨.𝗦.𝗦.𝗘.𝐅]❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @JOO_B_R_Z ❫
◉ 𝙸𝙳      : ❪ `6943111120` ❫
◉ 𝙱𝙸𝙾    : ❪ᥲ #ρᥱᖇ᥉᥆ꪀ Ꭵ᥉ #ժᥱ𝖋ᥱᥲƚᥱժ 𝖡ꪗ ƚᎻᥱ #ƚᎻᎥꪀᘜ᥉ Ꮋᥱ #ᥱꪎᥲᘜᘜᥱᖇᥲƚᥱ᥉ 𝐂𝐇 ⦂ J_GGC.t.me❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗬.𝗢.𝗨.𝗦.𝗦.𝗘.𝐅", url=f"https://t.me/JOO_B_R_Z"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url=f"https://t.me/BPHEE"),
                ],

            ]

        ),

    )
