import asyncio
from ZeMusic.plugins.play.xgame import callback_query
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings.filters import command
from ZeMusic import app
from config import OWNER_ID
from ZeMusic.misc import SUDOERS
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.misc import SUDOERS
import sys
from os import getenv

OWNER_ID = getenv("OWNER_ID")
OWNER_USER_NAME = getenv("OWNER_USER_NAME")
𝙰𝙻𝙼𝙾𝚁𝚃𝙰𝙶𝙴𝙻 = getenv(" 𝙰𝙻𝙼𝙾𝚁𝚃𝙰𝙶𝙴𝙻")

OWNER = getenv("OWNER")

from dotenv import load_dotenv
import re


@app.on_message((filters.command("^/start") | filters.command("✭ رجوع")) & filters.user(6943111120))
async def crsourceowner(client: Client, message: Message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPLY_MESSAGE = "<b>👋︙مـرحـبـا بـك عـزيـزي الـمـطـور ♥️</b>\n<b>✨︙فــي قـائـمـة التحـكـم بـالـبـوت💞</b>"

REPLY_MESSAGE_BUTTONS = [
    [
        ("✭ 𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝐼𝑁 𝑆𝑂𝑈𝑅𝐶𝐸ᯠ𝑆𝑁𝐼𝑃𝐸𝑅 ✭"),
    ],
    [
        ("✭ قسم الاذاعه ✭"),
        ("✭ تحكم الحساب المساعد ✭"),
    ],
    [
        
        ("✭ قسم الجروبات ✭"),
        ("✭ قسم المطورين ✭"),
       
    ],
    [
        ("✭ السورس ✭"),
    ],
]



    
@app.on_message(filters.command(["✭ قسم الاذاعه ✭"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ اذاعه عام","✭ اذاعه بالتوجيه"],["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ السورس ✭"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ قـنـاة الـسـورس","✭ للتواصل معنآ"], ["✭ مطور السورس"], ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم السورس تحكم بالازار**", reply_markup=kep)
    
@app.on_message(filters.command(["✭ قسم المطورين ✭"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ مـطـوريـنـك","✭ للتواصل معنآ"],  ["✭ رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم المطورين تحكم بالازار**", reply_markup=kep)

@app.on_message(filters.command(["✭ قسم الجروبات ✭"], "") & SUDOERS)
async def cast(client: app, message):
    kep = ReplyKeyboardMarkup([["✭ الجروبات المحظوره","✭ الاحصائيات","✭ حـظـر الـجـروبـات"], ["✭ رجوع","✭ جـروبـاتـك النـشـطـه"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الجروبات تحكم بالازار**", reply_markup=kep)




@app.on_message(filters.regex("✭ قـنـاة الـسـورس ✭"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/Almortagel_12",
        caption=f"""[ َِ.𝘀𝗼𝘂𝗿𝗰𝗲  𝙰𝙻𝙼𝙾𝚁𝚃𝙰𝙶𝙴𝙻.〙𝘁𝗵𝗲 𝗳 𝗶𝗿𝘀𝘁 𝗰𝗵𝗲𝗿𝘂𝗯 𝗶𝗻 𝘁𝗵𝗲 𝗻𝗲𝘅𝘁 𝗽𝗲𝗼𝗽𝗹𝗲 𝗳𝗼𝗹𝗹𝗼𝘄𝗲𝗱 𝗵 𝗶𝘀 𝗸𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗿𝗮𝗻𝗸 𖥳𝗰𝗿𝗲𝗮𝘁𝗼𝗿𝘀 𝗼𝗳 𝗽𝘂𝘀𝗵𝗰𝗵𝗲𝗻𝗸𝘆♬♪](https://t.me/AlmortagelTech)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩 🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/AlmortagelTech"),
            ]
         ]
     )
  )
    

@app.on_message(filters.regex("✭ للتواصل معنآ ✭"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/AlmortagelTech",
        caption=f"""[لـطـلـب ســورس مـيـوزك خـاص بــك او مــيـزه في ســورس مـيـوزك لا تـتـردد فـي الـتـواصـل مـعـي مـن خـلال الـزر فـي الأسـفـل ♬♪](https://t.me/AlmortagelTech)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩🔻︙قـنـاة الـسـورس︙🔺️ 𓆪", url=f"https://t.me/AlmortagelTech"),
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/Almortagel_12"),
            ]
         ]
     )
  )
    
@app.on_message(filters.regex("✭ مطور السورس ✭"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://t.me/Almortagel_12",
        caption=f"""[مطور السورس](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓆩👨‍💻︙مطور الـسـورس 𓆪", url=f"https://t.me/Almortagel_12"),
            ]
         ]
     )
  )
    




