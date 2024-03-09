import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import app
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
    command(["المطور مارو","مارو","المبرمج"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("j_s_9")
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
    command(["سورس","السورس","يا سورس"])
    & filters.group
    & ~filters.edited_message
    )
@app.on_message(
    command(["سورس","السورس","يا سورس"])
    & filters.channel
    & ~filters.edited_message
    )
@app.on_message(
    command(["سورس","السورس","يا سورس","قناة","قناه"])
    & filters.private
    & ~filters.edited_message
    )
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/09e50c75b48945d209829.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ](t.me/N_G_12)
么 [َժᥱ᥎ ꪀᥲ️ժᥱᖇ](t.me/Ng_103)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/Ng_333)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ժᥱ᥎ ꪀᥲ️ժᥱᖇ . 🕷 › ", url=f"https://t.me/Ng_103"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/N_G_12"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/Ng_333"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )

@app.on_message(command(["تخ"]) & filters.group)
async def huhh(client, message):
    to_id = int(ahmed.split("to")[-1].split("in")[0])
    from_id = int(ahmed.split("ahmed")[-1].split("to")[0])
    in_id = int(caption.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    ahmed = message.text
    await message.reply_animation(
        animation=f"https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""↯︙قتل ↫ ⦗ {app.get_chat(to_id).first_name}]({to_url}) ⦘\nالضحيه دا 😢 ↫ ⦗ [{app.get_chat(from_id).first_name}]({from_url}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
    )
    reply_markup=InlineKeyboardMarkup(

       [
           [
               InlineKeyboardButton(
                   "‹ : 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥 : ›", url=f"https://t.me/BPHEE"),
           ],
       ]
    ),
