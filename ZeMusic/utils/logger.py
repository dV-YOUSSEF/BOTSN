from pyrogram.enums import ParseMode

from ZeMusic import app
from ZeMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""━━━━━━━━━━━━━━━
◍ [⌞ 𝘾𝙍 𖢻 ⌯ 𝙈𝙐𝙎𝙄𝘾 ⌯  🎧💚   
━━━━━━━━━━━━━━━
🌹️ اسم المجموعة : > {message.chat.title} [{message.chat.id}]
━━━━━━━━━━━━━━━
🥀 اسم المستخدم : › {message.from_user.mention}
━━━━━━━━━━━━━━━
🌸 يوزر المستخدم : › @{message.from_user.username}
━━━━━━━━━━━━━━━
🌷 ايدي المستخدم  : › {message.from_user.id}
━━━━━━━━━━━━━━━
🌿 رابط الجروب: > {chatusername}
━━━━━━━━━━━━━━━
🌻 المطلوب: {message.text}
━━━━━━━━━━━━━━━
💐 نوع التشغيل: {streamtype}
━━━━━━━━━━━━━━━"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
