from pyrogram import Client, filters
from datetime import datetime
import pytz
from strings.filters import command
from DAXXMUSIC import app

def get_current_time():
    tz = pytz.timezone('Africa/Cairo')  # تعيين التوقيت لأفريقيا/القاهرة
    current_time = datetime.now(tz)
    return current_time.strftime("%p: %I:%M:%S\n\n%Y-%m-%d\n\n%Z%z")

@app.on_message(command(["/Time","الوقت","وقت"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"**⛥━━━━━( توقيت مصر  )━━━━━━⛥\n\n{time}**")
