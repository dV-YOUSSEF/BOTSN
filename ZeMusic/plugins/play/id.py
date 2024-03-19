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
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import ChatMemberStatus
from pyrogram.types import CallbackQuery

iddof = []

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(_, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in iddof:
            return await message.reply_text("**♪ الامر معطل من قبل  💎 .**")
        iddof.append(message.chat.id)
        return await message.reply_text("**♪ تم تعطيل الايدي بنجاح  💎 .**")
    else:
        return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(_, message):
    get = await app.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if not message.chat.id in iddof:
            return await message.reply_text("**♪ الايدي مفعل من قبل  💎 .**")
        iddof.remove(message.chat.id)
        return await message.reply_text("**♪ تم تفعيل الايدي بنجاح  💎 .**")
    else:
        return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client, message):
    if message.chat.id in iddof:
        return await message.reply_text("**♪ تم تعطيل امر الايدي من قبل المشرفين  💎 .**")
    user = await app.get_chat(message.from_user.id)
    user_id = user.id
    username = user.username
    first_name = user.first_name
    bioo = user.bio
    photo = user.photo.big_file_id
    photo = await app.download_media(photo)
    idd = len(id.get(user_id, []))
    await message.reply_photo(
        photo=photo,
        caption=f"**name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")],]
        ),
    )

id = {}

@app.on_callback_query(filters.regex("heart"))
async def heart(_, query: CallbackQuery):
    callback_data = query.data.strip()
    callback_request = callback_data.replace("heart", "")
    user_id = int(callback_request)
    user = await app.get_chat(user_id)
    if not query.from_user.mention in id.get(user_id, []):
        id[user_id] = id.get(user_id, []) + [query.from_user.mention]
    else:
        id[user_id].remove(query.from_user.mention)
    idd = len(id.get(user_id, []))
    await query.edit_message_text(
        f"**name : {user.first_name}\nid : {user_id}\nuser : [@{user.username}]\nbio : {user.bio}**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(f"{idd} 🤍", callback_data=f"heart{user_id}")]]
        ),
    )

app.run()
