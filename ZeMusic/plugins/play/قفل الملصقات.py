from ZeMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

stiklok = []

@app.on_message(
    filters.command(["قفل_الملصقات", "تعطيل_الملصقات"])
)
async def block_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفلة من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} أنت لست مشرفا")

@app.on_message(
    filters.command(["فتح_الملصقات", "تفعيل_الملصقات"])
)
async def unblock_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مفتوحة من قبل")
        stiklok.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} أنت لست مشرفا")