import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from ZeMusic import app
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from pyrogram.types import Message

lokrf = []


   @app.on_message(
     filters.command(["قفل الصور", "تعطيل الصور"])
     & filters.group
)
async def close_photos(client: Client, message: Message):
    if message.chat.id in lokrf:
        return await message.reply_text(f"**الصور مقفلة بالفعل في هذه المجموعة**")
    
    lokrf.append(message.chat.id)
    return await message.reply_text(f"**تم قفل إرسال الصور بنجاح في هذه المجموعة**")

      # قفل إرسال الصور في المجموعة
        await client.set_chat_permissions(
            message.chat.id,
            can_send_messages=True,
            can_send_media_messages=False,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
        )
    else:
        await message.reply_text("**عذراً، يجب أن تكون مشرفاً لتنفيذ هذا الأمر**")

@app.on_message(
    filters.command(["فتح الصور", "تفعيل الصور"])
    & filters.group
)
async def open_photos(client: Client, message: Message):
    if message.chat.id not in lokrf:
        return await message.reply_text(f"**إرسال الصور مفعل بالفعل في هذه المجموعة**")
    
    lokrf.remove(message.chat.id)
    return await message.reply_text(f"**تم فتح إرسال الصور بنجاح في هذه المجموعة**")

        # إعادة فتح إرسال الصور في المجموعة
        await client.set_chat_permissions(
            message.chat.id,
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_polls=True,
            can_send_other_messages=True,
            can_add_web_page_previews=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
        )
    else:
        await message.reply_text("**عذراً، يجب أن تكون مشرفاً لتنفيذ هذا الأمر**")

if __name__ == "__main__":
    app.run()  
