import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.raw import types
from ZeMusic import app
from datetime import datetime
import requests
import pytz
from ZeMusic.core.call import Mody
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pyrogram.errors import (
    ChatAdminRequired,
    UserAlreadyParticipant,
    UserNotParticipant,
)

adox = pytz.timezone('Africa/Cairo')

chat = []

@app.on_message(filters.text & ~filters.private, group = 20)
async def azaan(c, msg):
  if msg.text == "تفعيل الاذان":
    if msg.chat.id in chat:
      return await msg.reply_text("- الاذان متفعل اصلا يصحبي ♡.")
    else:
      chat.append(msg.chat.id)
      return await msg.reply_text("تم تفعيل الاذان ♡. ")
  elif msg.text == "تعطيل الاذان":
    if msg.chat.id in chat:
      chat.remove(msg.chat.id)
      return await msg.reply_text("تم تعطيل الاذان ♡. ")
    else:
      return await msg.reply_text("- الاذان متعطله اصلا يصحبي ♡.")
           
async def kill():
  for i in chat:
    await Mody.force_stop_stream(i)


async def play(i):
  assistant = await group_assistant(Mody,i)
  file_path = "./ZeMusic/assets/azan.mp3"
  stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
  try:
      await assistant.join_group_call(i,
           stream,
           stream_type=StreamType().pulse_stream,
      )
  except NoActiveGroupCall:
    try:
        await Mody.join_assistant(i,i)
    except Exception as e:
       await app.send_message(i,f"{e}")
  except TelegramServerError:
    await app.send_message(i,"اسف في شوين مشاكل في سرفر التلجرام")
  except AlreadyJoinedError:
    await kill()
    try:
        await assistant.join_group_call(i,
           stream,
           stream_type=StreamType().pulse_stream,
        )
    except Exception as e:
        await app.send_message(i,f"{e}")
  
    
def prayer_time():
   try:
       prayer = requests.get(f"http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0")
       prayer = prayer.json()
       fajr = datetime.strptime(prayer['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
       dhuhr = datetime.strptime(prayer['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
       asr = datetime.strptime(prayer['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
       maghrib = datetime.strptime(prayer['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
       isha = datetime.strptime(prayer['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')
       if datetime.now(adox).strftime('%I:%M %p') == fajr:
         return "الفجر"
       elif datetime.now(adox).strftime('%I:%M %p') == dhuhr:
         return "الظهر"
       elif datetime.now(adox).strftime('%I:%M %p') == asr:
         return "العصر"
       elif datetime.now(adox).strftime('%I:%M %p') == maghrib:
         return "المغرب"
       elif datetime.now(adox).strftime('%I:%M %p') == isha:  
         return "العشاء" 
   except Exception as e:
       asyncio.sleep(4)
       print(e)        
      
async def azan():
  while not await asyncio.sleep(1):
    if prayer_time():
     prayer = prayer_time()
     await kill()
     for i in chat:
       await app.send_message(i, f"حان الان وقت اذان {prayer} بتوقيت القاهره 🕊❤. ")
       await play(i)
     await asyncio.sleep(177)
     await kill()
