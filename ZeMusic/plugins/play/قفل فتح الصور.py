import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from ZeMusic import app
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

lokrf = []

@app.on_message(
     filters.command(["قفل الصور", "تعطيل الصور"])
     & filters.group
)
async def close_photos(client: Client, message: Message):
    dev = [OWNER_ID]
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطور أساسي"
    elif get.status == ChatMemberStatus.OWNER:
        rotba = "المالك"
    elif get.status == ChatMemberStatus.ADMINISTRATOR:
        rotba = "أدمن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention}، أنت لست مشرفاً هنا**")
        
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if message.chat.id in lokrf:
            return await message.reply_text(f"**يا {message.from_user.mention}، الصور مقفلة بالفعل**")
        lokrf.append(message.chat.id)
        return await message.reply_text(f"**تم قفل إرسال الصور بنجاح\n\nبواسطة {rotba} ← {message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention}، أنت لست مشرفاً هنا**")

@app.on_message(
    filters.command(["فتح الصور", "تفعيل الصور"])
    & filters.group
)
async def open_photos(client: Client, message: Message):
    dev = [OWNER_ID]
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطور أساسي"
    elif get.status == ChatMemberStatus.OWNER:
        rotba = "المالك"
    elif get.status == ChatMemberStatus.ADMINISTRATOR:
        rotba = "أدمن"
    else:
        return await message.reply_text(f"**يا {message.from_user.mention}، أنت لست مشرفاً هنا**")
    
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if not message.chat.id in lokrf:
            return await message.reply_text(f"**يا {message.from_user.mention}، إرسال الصور مفعل بالفعل**")
        lokrf.remove(message.chat.id)
        return await message.reply_text(f"**تم فتح إرسال الصور بنجاح\n\nبواسطة {rotba} ← {message.from_user.mention}**")

if __name__ == "__main__":
    app.run()
