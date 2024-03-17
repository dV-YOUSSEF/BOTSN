import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import OWNER_ID, BANNED_USERS
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

# تحديد الرسالة التي ستُرسل في حالة الرد على الأمر "start"
REPLY_MESSAGE = "اليك الكيب مطوري العزيز ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​🌝💚"

# تحديد الأزرار التي ستظهر في الكيبورد
REPLY_MESSAGE_BUTTONS = [
    [
        ("• السورس •")
    ],
    [
        ("• المطور •"),
        ("• مطور السورس •")
    ],
    [
        ("• تويت •"),
        ("• صراحه •") 
    ],
    [
        ("• 🤍​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​🌝 •") 
    ],
    [
        ("• اسئله •"),
        ("• امثله •") 
    ],
    [
        ("• نكته •"),
        ("• فزوره •")
    ],
    [
        ("• 💚​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​🌝 •")
    ],
    [
        ("• اعلام •"),
        ("• تفكيك •")
    ],
    [
        ("• رمزيه •"),
        ("• صور •")         
    ],
    [
        ("• عقاب •"),
        ("• تحدي •")
    ],
    [
        ("• لو خيروك •")
    ],
    [           
        ("ꨄ حذف الكيبورد ꨄ")
    ]
]

# دالة لفتح الكيبورد عند الأمر "start"
@app.on_message(filters.command(["start"], "") & filters.private & ~BANNED_USERS)
async def madison(client: Client, message: Message): 
    # التحقق مما إذا كان المرسل مطور البوت
    if message.from_user.id == :
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
        await message.reply(
            text=text,
            reply_markup=reply_markup
        )

# دالة لحذف الكيبورد
@app.on_message(filters.command(["ꨄ حذف الكيبورد ꨄ"], "") & filters.user(OWNER_ID))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

# بدء تشغيل البوت
app.run()
