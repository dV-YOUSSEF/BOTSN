import asyncio
import os
import time
import requests
from pyrogram import filters
import random
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

@Client.on_message(filters.command(["المطور", "مطور","مطور البوت"], ""))
async def dev(client: Client, message: Message):
     if await joinch(message):
            return
     bot_username = client.me.username
     dev = await get_dev(bot_username)
     user = await client.get_chat(chat_id=dev)
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     
     # استخدام الرابط للفيديو
     video_url = "https://telegra.ph/file/0beba425b2965d6dea71e.mp4"
     
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور الأساسي**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
        pass
     
     # إرسال الفيديو كرسالة
     try:
         await client.send_video(chat_id=message.chat.id, video=video_url, caption=f"**Developer Name : {name}** \n**Devloper Username : @{username}**\n**{bio}**",
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     except:
         pass
    
@app.on_message(
    command(["سورس","السورس"])

)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/48a480ba73bdc472b9de1.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ ᥉᥆υᖇᥴᥱ ᥉ꪀᎥρᥱᖇ](t.me/BPHEE)
么 [َժᥱ᥎ ꪀᥲ️ժᥱᖇ](t.me/JOO_B_R_Z)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/B_X_N1)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
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
