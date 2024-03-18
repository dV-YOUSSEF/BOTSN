@app.on_message(command(["اذاعه", "/broadcast", "ذيع"]) & SUDOERS)
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING
    if message.reply_to_message:
        if hasattr(message.reply_to_message, 'message_id'):
            x = message.reply_to_message.message_id
            y = message.chat.id
        else:
            # إذا لم يكن للرسالة رد، أو إذا كانت الرسالة الرد عليها ليست من نوع Message
            return await message.reply_text("يرجى الرد على الرسالة التي ترغب في إرسالها.")
    else:
        # في حالة عدم وجود رسالة رد
        return await message.reply_text("يرجى الرد على الرسالة التي ترغب في إرسالها.")

    if len(message.command) < 2:
        return await message.reply_text(_["broad_2"])

    query = message.text.split(None, 1)[1]
    pin_message = False
    forward_message = False
    if "بالتثبيت" in query:
        query = query.replace("بالتثبيت", "")
        pin_message = True
    elif "بالتحويل" in query:
        query = query.replace("بالتحويل", "")
        forward_message = True

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

    # إرسال الرسالة وتحديد السلوك المطلوب
    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if pin_message:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except Exception as e:
                        print(f"Failed to pin message: {e}")
                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception as e:
                print(f"Failed to send message: {e}")
                continue
        try:
            await message.reply_text(_["broad_3"].format(sent, pin))
        except:
            pass

    # إذا كانت هناك كلمة مفتاحية -user في الرسالة
    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                flood_time = int(fw.value)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except:
                pass
        try:
            await message.reply_text(_["broad_4"].format(susr))
        except:
            pass

    # إذا كانت هناك كلمة مفتاحية -assistant في الرسالة
    if "-assistant" in message.text:
        aw = await message.reply_text(_["broad_5"])
        text = _["broad_6"]
        from ZeMusic.core.userbot import assistants

        for num in assistants:
            sent = 0
            client = await get_client(num)
            async for dialog in client.get_dialogs():
                try:
                    await client.forward_messages(
                        dialog.chat.id, y, x
                    ) if message.reply_to_message else await client.send_message(
                        dialog.chat.id, text=query
                    )
                    sent += 1
                    await asyncio.sleep(3)
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue
            text += _["broad_7"].format(num, sent)
        try:
            await aw.edit_text(text)
        except:
            pass
    IS_BROADCASTING = False
