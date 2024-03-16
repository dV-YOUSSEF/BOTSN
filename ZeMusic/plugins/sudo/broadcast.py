import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from strings.filters import command
from ZeMusic import app
from ZeMusic.misc import SUDOERS
from ZeMusic.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from ZeMusic.utils.decorators.language import language
from ZeMusic.utils.formatters import alpha_to_int
from config import adminlist

IS_BROADCASTING = False

@app.on_message(command(["اذاعة","/forward", "اذاعه", "ذيع"]) & SUDOERS)
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.text.split()) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-assistant" in query:
            query = query.replace("-assistant", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if query == "":
            return await message.reply_text(_["broad_8"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
        for chat_id in chats:
            try:
                m = (await app.forward_messages(chat_id, y, x)) if message.reply_to_message else (await app.send_message(chat_id, text=query))
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except:
                        continue
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                continue
        try:
            await message.reply_text(_["broad_3"].format(sent, pin))
        except:
            pass

    if "-user" in message.text:
        susr = 0
        served_users = [int(user["user_id"]) for user in await get_served_users()]
        for user_id in served_users:
            try:
                m = (await app.forward_messages(user_id, y, x)) if message.reply_to_message else (await app.send_message(user_id, text=query))
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
        try:
            await message.reply_text(_["broad_4"].format(susr))
        except:
            pass

    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_5"])
        text = _["broad_6"]
        from ZeMusic.core.userbot import assistants

        async def forward_messages_to_assistants(client, dialog_chat_id, message_id, query_text):
            sent_count = 0
            async for dialog in client.iter_dialogs():
                try:
                    await client.forward_messages(dialog_chat_id, y, message_id) if message.reply_to_message else await client.send_message(dialog_chat_id, text=query_text)
                    sent_count += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            return sent_count

        for num in assistants:
            client = await get_client(num)
            sent_count = await forward_messages_to_assistants(client, message.chat.id, x, query)
            text += _["broad_7"].format(num, sent_count)
        try:
            await aw.edit_text(text)
        except:
            pass
    IS_BROADCASTING = False

async def auto_clean():
    while True:
        await asyncio.sleep(10)
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.iter_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS):
                        if user.status == 'creator' or user.status == 'administrator':
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except Exception as e:
            print(f"Error in auto_clean: {e}")
            continue

asyncio.create_task(auto_clean())
