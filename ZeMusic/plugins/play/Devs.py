import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import enums
from pyrogram import types
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import app
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
    command(["المطور","جولدن","يوسف","مطور السورس","مبرمج السورس"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("JOO_B_R_Z")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"– – – – – – – – – – – – – – – – – –\n↯︙𝖣𝖾𝗏 ↬ ⦗ {name} ⦘\n↯︙𝖴𝗌𝖤𝗋 ↬ ⦗ @{usr.username} ⦘\n↯︙𝖨𝖣 ↬ ⦗ {usr.id} ⦘\n↯︙𝖡𝗂𝖮 ↬ ⦗ {usr.bio} ⦘\n– – – – – – – – – – – – – – – – – –",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["سورس","السورس"])

)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/48a480ba73bdc472b9de1.jpg",caption=f"╭═★⊷⌯⧼[𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂](https://t.me/CMG_5S)⧽⌯⊶★═╮\n★‹ [𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂](https://t.me/CMG_5S)\n★‹ [𝐀𝐒𝗞 𝗧𝐎 𝐌𝗘](https://t.me/M_Q_ll)\n★‹ [𝐓𝐨𝐱𝐢𝐂](https://t.me/M_Q_ll)\n★‹ [𝐓𝐎.𝐌𝐄](https://t.me/GROUP_CAPTAIN)\n╰═★⊷⌯⧼[𝐒𝐨𝐮𝐑𝐜𝐞𝐓𝐨𝐱𝐢𝐂](https://t.me/CMG_5S)⧽⌯⊶★═╯",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/maro_pro"), 
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/BPHEE"),
                  ],[
                    InlineKeyboardButton(
                        " 𝗬.𝗢.𝗨.𝗦.𝗦.𝗘.𝐅 ", url=f"https://t.me/JOO_B_R_Z"),
                  ],[
                    InlineKeyboardButton(
                        ".💘اضف البوت اللي مجموعتك", url=f"https://t.me/{app.username}?startgroup=true"),
                ],
            ]
        ),
        parse_mode=enums.ParseMode.MARKDOWN
    )
@app.on_message(filters.command(["تخ"]) & filters.group)
async def huhh(client, message):
    ahmed = message.text
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(ahmed.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحية دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
        reply_markup=InlineKeyboardMarkup(
           [
               [
                   InlineKeyboardButton(
                       "‹ : 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥 : ›", url=f"https://t.me/BPHEE"),
               ],
           ]
        ),
    )
