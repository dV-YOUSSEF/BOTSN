import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait

ahmed = {}
tom_max = 3

@app.on_message(filters.command("انذار", ""))
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"{ahmed[chat_id][user_id]}")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
            del ahmed[chat_id][user_id]
            await client.ban_chat_member(chat_id, user_id)
            await message.reply("تم طرد العضو")        
        except:
            await message.reply("لم يتم مظر العضو")
    else:
        warnings_left = tom_max - ahmed[chat_id][user_id]
        await message.reply(f"لقد تم اعطاء العضو انذار، وتبقى له {warnings_left} انذارات حتى يتم الطرد.")
        
        if ahmed[chat_id][user_id] == tom_max - 1:
            # إرسال لوحة مفاتيح بعد الانذار الأخير
            keyboard = [
                [
                    {"text": "كتم", "callback_data": "mute"},
                    {"text": "طرد", "callback_data": "kick"},
                    {"text": "حظر", "callback_data": "ban"}
                ]
            ]
            await message.reply("لقد وصلت إلى الحد الأقصى لعدد الإنذارات. اختر الإجراء الذي تريده:", reply_markup={"inline_keyboard": keyboard})

@app.on_callback_query(filters.regex("mute"))
async def mute_user(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.message.reply_to_message.from_user.id
    try:
        await client.restrict_chat_member(chat_id, user_id, permissions=ChatPermissions())
        await callback_query.answer("تم كتم العضو")
    except:
        await callback_query.answer("حدث خطأ أثناء محاولة كتم العضو")

@app.on_callback_query(filters.regex("kick"))
async def kick_user(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.message.reply_to_message.from_user.id
    try:
        await client.kick_chat_member(chat_id, user_id)
        await callback_query.answer("تم طرد العضو")
    except:
        await callback_query.answer("حدث خطأ أثناء محاولة طرد العضو")

@app.on_callback_query(filters.regex("ban"))
async def ban_user(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.message.reply_to_message.from_user.id
    try:
        await client.kick_chat_member(chat_id, user_id)
        await client.unban_chat_member(chat_id, user_id)
        await callback_query.answer("تم حظر العضو")
    except:
        await callback_query.answer("حدث خطأ أثناء محاولة حظر العضو")
        
        


