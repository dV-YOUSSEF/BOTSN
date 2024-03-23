from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app
from config import OWNER_ID
import asyncio
import aiohttp
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMusic.core.call import Mody 
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

# Function to create inline keyboard
def create_keyboard():
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(" اغلاق ", callback_data="close_vc")]])
    return keyboard


@app.on_message(filters.regex("^مين في الكول$"))
async def strcall(client, message):
    assistant = await group_assistant(Mody,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./ZeMusic/assets/call.mp3"), stream_type=StreamType().pulse_stream)
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣 "
            else:
                mut="ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"عمووووو الكول مش مفتوح اصلااا\n❌")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n❌")
    except AlreadyJoinedError:
        text="🔔 الاعضاء المتواجدين في الكول :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕 "
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("<b>𖠇 تم بدء المحادثه الصوتيه..✅</b>\n<b>│</b>\n<b>└𖠇 بواسطة الادمنيه 👨‍✈️ </b>", reply_markup=create_keyboard())
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("<b>𖠇 تم بدء المحادثه الصوتيه..✅</b>\n<b>│</b>\n<b>└𖠇 بواسطة الادمنيه 👨‍✈️ </b>", reply_markup=create_keyboard())
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {da} ثواني </b>", reply_markup=create_keyboard())        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : دقيقة </b>", reply_markup=create_keyboard())
        elif 2 <= ma[0] < 3:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : دقيقتين </b>", reply_markup=create_keyboard())
        elif 3 <= ma[0] < 11:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {ma[0]} دقايق </b>", reply_markup=create_keyboard())  
        else:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {ma[0]} دقيقه </b>", reply_markup=create_keyboard())
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : ساعه </b>", reply_markup=create_keyboard())
        elif 2 <= ho[0] < 3:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : ساعتين </b>", reply_markup=create_keyboard())
        elif 3 <= ho[0] < 11:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {ho[0]} ساعات </b>", reply_markup=create_keyboard())  
        else:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {ho[0]} ساعة </b>", reply_markup=create_keyboard())
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : يوم </b>", reply_markup=create_keyboard())
        elif 2 <= day[0] < 3:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : يومين </b>", reply_markup=create_keyboard())
        elif 3 <= day[0] < 11:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {day[0]} ايام </b>", reply_markup=create_keyboard())  
        else:
            await message.reply(f"<b>𖠇 تم انهاء المحادثه الصوتيه..❎</b>\n<b>│</b>\n<b>└𖠇 وقت المحادثة : {day[0]} يوم</b>", reply_markup=create_keyboard())
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• قــــام ← {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n• بــدعـــوة ←{user.first_name}"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass
