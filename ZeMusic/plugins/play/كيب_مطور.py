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

@app.on_message(command(["start", "✭ رجوع"]) & SUDOERS)

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
    

OFFPV = []

@app.on_message(filters.command(["تفعيل التواصل","تعطيل التواصل"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER or message.from_user.id == dev:
        text = message.text
        if text == "تفعيل التواصل":
          if not client.me.username in OFFPV:
             await message.reply_text("**♪ التواصل مفعل من قبل  💎 .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("**♪ تم تفعيل التواصل  💎 .**")
            return
          except:
             pass
        if text == "تعطيل التواصل":
          if client.me.username in OFFPV:
             await message.reply_text("**♪ التواصل معطل من قبل  💎 .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("**♪ تم تعطيل التواصل  💎 .**")
            return
          except:
             pass


@app.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**♪ تم ارسال رساتلك إلي {u.mention} بنجاح  💎 .**")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER[0], message.chat.id, message.id)
   except Exception as e:
     pass

 message.continue_propagation()


