# استيراد الوحدات اللازمة
from pyrogram import Client, filters
from datetime import datetime
import pytz
from strings.filters import command
from ZeMusic import app

# دالة للحصول على الوقت الحالي بتوقيت مصر
def get_current_time():
    tz = pytz.timezone('Africa/Cairo')
    current_time = datetime.now(tz)
    return current_time.strftime("<b>%p: %I:%M:%S</b>\n\n<b>%Y-%m-%d</b>\n\n<b>%Z%z</b>")

# تعريف دالة التفاعل مع الأمر المرسل
@app.on_message(command(["/Time","الوقت","وقت"]))
async def send_time(client, message):
    # الحصول على الوقت الحالي
    time = get_current_time()
    # إرسال الرسالة بالوقت المحدد إلى المحادثة
    await client.send_message(message.chat.id, f"<b>≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫\n\n{time}")
