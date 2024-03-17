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
from ZeMusic.core.call import Anony
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

tz = pytz.timezone('Africa/Cairo')
chat = []

async def kill():
    for i in chat:
        await Anony.force_stop_stream(i)

async def play(i):
    assistant = await group_assistant(Anony, i)
    file_path = "./ZeMusic/assets/azan.m4a"
    stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
    try:
        await assistant.join_group_call(
            i,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        try:
            await Anony.join_assistant(i, i)
        except Exception as e:
            await app.send_message(i, f"{e}")
    except TelegramServerError:
        await app.send_message(i, "في خطا ف سيرفرات التليجرام")
    except AlreadyJoinedError:
        await kill()
        try:
            await assistant.join_group_call(
                i,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except Exception as e:
            await app.send_message(i, f"{e}")

async def azkar():
    while True:
        await asyncio.sleep(2)
        prayer = prayer_time()
        if prayer:
            await kill()
            for i in chat:
                await app.send_message(i, f"حان الآن وقت الأذان لصلاة {prayer} بالتوقيت المحلي للقاهرة 🥰♥️")
                await play(i)
            await asyncio.sleep(174)
            await kill()

def prayer_time():
    try:
        prayer = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0")
        prayer = prayer.json()
        fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%H:%M')
        dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%H:%M')
        asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%H:%M')
        maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%H:%M')
        isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%H:%M')
        current_time = datetime.now(tz).strftime('%H:%M')
        if current_time == fajr:
            return "الفجر"
        elif current_time == dhuhr:
            return "الظهر"
        elif current_time == asr:
            return "العصر"
        elif current_time == maghrib:
            return "المغرب"
        elif current_time == isha:
            return "العشاء"
    except Exception as e:
        print(e)

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

asyncio.create_task(azkar())
#مواعيد الصلاه بس الي سارقها بقيت الكود كتابتي هي اكيد كتابه معاقه بس عادي م مهم رايك انا مبسوط بيها يوزري للاعمال الخاصه @z0hary
     
