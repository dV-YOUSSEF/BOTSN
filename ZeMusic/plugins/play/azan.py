import asyncio
import pytz
import requests
from datetime import datetime
from pyrogram import filters
from pyrogram.raw import types
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from ZeMusic import app
from ZeMusic.core.call import DAXX
from ZeMusic.utils.database import group_assistant, HighQualityAudio

tz = pytz.timezone('Africa/Cairo')
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

# توقيت الصلاة وتشغيل الأذان
async def prayer_time():
    try:
        response = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0")
        if response.status_code == 200:
            prayer = response.json()['data']['timings']
            fajr = prayer['Fajr']
            dhuhr = prayer['Dhuhr']
            asr = prayer['Asr']
            maghrib = prayer['Maghrib']
            isha = prayer['Isha']
            now_time = datetime.now(tz).strftime('%I:%M %p')
            
            if now_time == fajr or now_time == dhuhr or now_time == asr or now_time == maghrib or now_time == isha:
                for chat_id in chat:
                    await app.send_message(chat_id, f"حان وقت الصلاة")
                await play_azaan()
    except Exception as e:
        print("An error occurred while fetching prayer time:", e)

# تشغيل الأذان
async def play_azaan():
    for chat_id in chat:
        assistant = await group_assistant(DAXX, chat_id)
        file_path = "./strings/azan.m4a"
        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await assistant.join_group_call(
                chat_id,
                stream,
                stream_type=StreamType().pulse_stream,
            )
        except Exception as e:
            print(f"Error occurred while playing Azan: {e}")

# تشغيل وظيفة الأذان
async def main():
    while True:
        await prayer_time()
        await asyncio.sleep(60)  # تحديث كل دقيقة

# تشغيل البرنامج
if __name__ == "__main__":
    asyncio.run(main())
