import asyncio
import random
from ZeMusic.misc import SUDOERS
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges)
from pyrogram import filters, Client
from ZeMusic import app
from config import *


MUSIC_BOT_NAME = {}
botname = {}

name = "فاست"

@app.on_message(filters.regex("تعيين اسم البوت") & filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

toxi_responses = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يحب",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك أكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي على النبي كدا",
    "مش فاضيلك نصايح وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    "ورحمة أبويا اسمي {name}",
]

@app.on_message(filters.command(["بوت", "البوت"]))
async def toxi_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(toxi_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")]
    ])

    await message.reply_text(
        text=f"{bar}",
        disable_web_page_preview=True,
        reply_markup=keyboard
    )
