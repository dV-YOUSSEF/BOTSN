import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from ZeMusic import app
import random
from datetime import datetime
import requests
import pytz
from ZeMusic.core.call import Mody
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

# تعريف المنطقة الزمنية للقاهرة
tz = pytz.timezone('Africa/Cairo')

# قائمة لتخزين معرفات المحادثات التي تم تفعيل الأذان فيها
chat = []

# تفعيل وتعطيل الأذان
@app.on_message(filters.text & ~filters.private, group=20)
async def azaan(c, msg):
    if msg.text == "تفعيل الاذان":
        if msg.chat.id in chat:
            return await msg.reply_text("- الاذان متفعل هنا من قبل 🥰♥️")
        else:
            chat.append(msg.chat.id)
            return await msg.reply_text("تم تفعيل الاذان ♥️🌿")
    elif msg.text == "تعطيل الاذان":
        if msg.chat.id in chat:
            chat.remove(msg.chat.id)
            return await msg.reply_text("تم تعطيل الاذان ♥️🌿")
        else:
            return await msg.reply_text("- الاذان متعطل هنا من قبل 🥰♥️")

# توقيت الصلاة
def prayer_time():
    try:
        # استدعاء API للحصول على توقيتات الصلاة
        prayer = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0")
        prayer = prayer.json()
        
        # تحويل توقيتات الصلاة إلى التنسيق المناسب
        fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
        dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
        asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
        maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
        isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')
        
        # الوقت الحالي بتوقيت القاهرة
        now_time = datetime.now(tz).strftime('%I:%M %p')
        
        # تحديد الصلاة الحالية
        if now_time == fajr:
            return "الفجر"
        elif now_time == dhuhr:
            return "الظهر"
        elif now_time == asr:
            return "العصر"
        elif now_time == maghrib:
            return "المغرب"
        elif now_time == isha:
            return "العشاء"
    except Exception as e:
        print(e)

# تشغيل الأذان
async def play(i):
    assistant = await group_assistant(Mody, i)
    file_path = "./ZeMusic/assets/azan.m4a"
    stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
    try:
        await assistant.join_group_call(
            i,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except Exception as e:
        await app.send_message(i, f"{e}")

# إرسال رسالة بوقت الأذان وتشغيل الأذان
async def azkar():
    while True:
        if prayer_time():
            prayer = prayer_time()
            # إرسال إشعار بوقت الصلاة للمحادثات التي تم تفعيل الأذان فيها
            await asyncio.gather(*[app.send_message(i, f"حان الان وقت اذان {prayer} بتوقيت القاهرة 🥰♥️") for i in chat])
            # تشغيل الأذان للمحادثات التي تم تفعيل الأذان فيها
            await asyncio.gather(*[play(i) for i in chat])
        # انتظار 174 ثانية (حوالي 3 دقائق) قبل التحقق مرة أخرى من وقت الصلاة
        await asyncio.sleep(174)

# تشغيل وظيفة الأذان
async def main():
    await azkar()

# تشغيل البرنامج
if name == "main":
    asyncio.run(main())