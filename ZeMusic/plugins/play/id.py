import asyncio
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram import ChatMemberStatus
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZeMusic import app
from ZeMusic.utils.database import is_on_off
from ZeMusic import app
import re
import sys
import os
import random
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




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







#@app.on_message(command(["ا"]) & filters.group &
#async def khalid(client: Client, message: Message):
    #usr = await client.get_users(message.from_user.id)
    #name = usr.first_name
    #async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    #await message.reply_photo(photo.file_id,       caption=f"""ᴜsᴇʀ -› {message.from_user.mention}\n𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲 -› @{message.from_user.username}\nɪᴅ -› {message.from_user.id}\nbio » {bio}""", 
        #reply_markup=InlineKeyboardMarkup(

            #[

                #[

                    #InlineKeyboardButton(

                        #name, url=f"https://t.me/{message.from_user.id}")

                #],

            #]

        #),

    #)

@app.on_message(filters.regex("^ا$") & filters.group)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""**↯ : وفي النهاية أنتم السيئون وهم الأبرياء**
            
**↯ : اسمك : › {message.from_user.mention}**
                    
**↯ : معرفك : › @{message.from_user.username}**
                    
**↯ : ايديك : › `{message.from_user.id}`**
                    
**↯ : البايو : › \n {bio}**""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                                            name, user_id=6581896306)
                ],

            ]

        ),

    )
    


iddof = []
id = {}

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in iddof:
            return await message.reply_text("♪ الامر معطل من قبل 💎 .")
        iddof.append(message.chat.id)
        return await message.reply_text("♪ تم تعطيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in iddof:
            return await message.reply_text("♪ الايدي مفعل من قبل 💎 .")
        iddof.remove(message.chat.id)
        return await message.reply_text("♪ تم تفعيل الايدي بنجاح 💎 .")
    else:
        return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط 💎 .")
        
    user = await client.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bio = user.bio
    chat = message.chat.title
    chat_id = message.chat.id
   
    photo = user.photo.big_file_id
    if photo:
        photo = await client.download_media(photo)
    else:
        photo = None
    
    if user.id not in id:
        id[user.id] = []
    
    idd = len(id[user.id])
    
    caption = f"┇‌ ⤹•ɴᴀᴍᴇ : {first_name}\n┇‌ ⤹•ᴜsᴇʀ : @{username}\n┇‌ ═══════『♡』═══════\n┇‌ ⤹•ɪᴅ : {user_id}\n┇‌ ⤹•ʙɪᴏ : {bio}\n┇‌═══════『♡』═══════\n┇‌ ⤹•ᴄʜᴀᴛ : {chat}\n┇‌ ⤹•ᴄʜᴀᴛ ɪᴅ : {chat_id}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await message.reply_photo(photo=photo, caption=caption, reply_markup=reply_markup)

@app.on_callback_query(filters.regex("heart"))
async def heart(client, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    user_id = int(callback_request)
    user = await client.get_chat(user_id)
    
    if user.id not in id:
        id[user.id] = []
    
    if query.from_user.mention not in id[user.id]:
        id[user.id].append(query.from_user.mention)
    else:
        id[user.id].remove(query.from_user.mention)
    
    idd = len(id[user.id])
    
    caption = f"┇‌ ⤹•ɴᴀᴍᴇ : {user.first_name}\n┇‌ ⤹•ᴜsᴇʀ : @{user.username}\n┇‌ ═══════『♡』═══════\n┇‌ ⤹•ɪᴅ : {user_id}\n┇‌ ⤹•ʙɪᴏ : {user.bio}\n┇‌═══════『♡』═══════\n┇‌ ⤹•ᴄʜᴀᴛ : {query.message.chat.title}\n┇‌ ⤹•ᴄʜᴀᴛ ɪᴅ : {query.message.chat.id}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]])
    
    await query.edit_message_text(caption, reply_markup=reply_markup)
    

