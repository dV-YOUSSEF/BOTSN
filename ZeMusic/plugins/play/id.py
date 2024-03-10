import asyncio
import pyrogram
from pyrogram import Client, filters
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
    
    
@Client.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "")& filters.group)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("**♪ الامر معطل من قبل  💎 .**")
      iddof.append(message.chat.id)
      return await message.reply_text("**♪ تم تعطيل الايدي بنجاح  💎 .**")
   else:
      return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@Client.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "")& filters.group)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("**♪ الايدي مفعل من قبل  💎 .**")
      iddof.remove(message.chat.id)
      return await message.reply_text("**♪ تم تفعيل الايدي بنجاح  💎 .**")
   else:
      return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@Client.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("**♪ تم تعطيل امر الايدي من قبل المشرفين  💎 .**")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"**name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")],]),)

