from strings.filters import command
from ZeMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
stiklok = []
photos_lock = []
forward_lock = []
link_lock = []
mention_lock = []

@app.on_message(filters.text & filters.regex(r'^(/|!|)قفل الملصقات$'))
async def block_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مقفلة من قبل")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"تم قفل الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'^(/|!|)فتح الملصقات$'))
async def unblock_stickers(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in stiklok:
            return await message.reply_text(f"يا {message.from_user.mention} الملصقات مفتوحة من قبل")
        stiklok.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الملصقات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.sticker)
async def delete_stickers(client:Client, message:Message):
    if message.chat.id in stiklok:
        await message.delete()


@app.on_message(filters.text & filters.regex(r'^(/|!|)قفل الصور$'))
async def block_photos(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in photos_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الصور مقفلة من قبل")
        photos_lock.append(message.chat.id)
        return await message.reply_text(f"تم قفل الصور \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'^(/|!|)فتح الصور$'))
async def unblock_photos(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in photos_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الصور مفتوحة من قبل")
        photos_lock.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الصور \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.photo)
async def delete_photos(client:Client, message:Message):
    if message.chat.id in photos_lock:
        await message.delete()


@app.on_message(filters.text & filters.regex(r'^(/|!|)قفل التوجيهات$'))
async def block_forwards(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in forward_lock:
            return await message.reply_text(f"يا {message.from_user.mention} التوجيهات مقفلة من قبل")
        forward_lock.append(message.chat.id)
        return await message.reply_text(f"تم قفل التوجيهات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'^(/|!|)فتح التوجيهات$'))
async def unblock_forwards(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in forward_lock:
            return await message.reply_text(f"يا {message.from_user.mention} التوجيهات مفتوحة من قبل")
        forward_lock.remove(message.chat.id)
        return await message.reply_text(f"تم فتح التوجيهات \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.forwarded)
async def delete_forwards(client:Client, message:Message):
    if message.chat.id in forward_lock:
        await message.delete()


@app.on_message(filters.text & filters.regex(r'^(/|!|)قفل الروابط$'))
async def block_links(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in link_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الروابط مقفلة من قبل")
        link_lock.append(message.chat.id)
        return await message.reply_text(f"تم قفل الروابط \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'^(/|!|)فتح الروابط$'))
async def unblock_links(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in link_lock:
            return await message.reply_text(f"يا {message.from_user.mention} الروابط مفتوحة من قبل")
        link_lock.remove(message.chat.id)
        return await message.reply_text(f"تم فتح الروابط \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'https?://\S+'))
async def delete_links(client:Client, message:Message):
    if message.chat.id in link_lock:
        await message.delete()
        

@app.on_message(filters.text & filters.regex(r'^(/|!|)قفل المنشن$'))
async def block_mentions(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in mention_lock:
            return await message.reply_text(f"يا {message.from_user.mention} المنشن مقفل من قبل")
        mention_lock.append(message.chat.id)
        return await message.reply_text(f"تم قفل المنشن \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.text & filters.regex(r'^(/|!|)فتح المنشن$'))
async def unblock_mentions(client:Client, message:Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id not in mention_lock:
            return await message.reply_text(f"يا {message.from_user.mention} المنشن مفتوح من قبل")
        mention_lock.remove(message.chat.id)
        return await message.reply_text(f"تم فتح المنشن \n\n من قبل ←{message.from_user.mention}")
    else:
        return await message.reply_text(f"يا {message.from_user.mention} انت لست مشرفا")

@app.on_message(filters.entity("mention"))
async def delete_mentions(client:Client, message:Message):
    if message.chat.id in mention_lock:
        await message.delete()
        
