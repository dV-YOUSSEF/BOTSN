from pyrogram import Client, filters
from datetime import datetime
import pytz
from strings.filters import command
from ZeMusic import app

def get_current_time():
    tz = pytz.timezone('Africa/Cairo')  # تعيين التوقيت لأفريقيا/القاهرة
    current_time = datetime.now(tz)
    return current_time.strftime("<b>%p: %I:%M:%S</b>\n\n<b>%Y-%m-%d</b>\n\n<b>%Z%z</b>")

@app.on_message(command(["/Time","الوقت","وقت"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"<b>≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫</b>\n\n{time}")
