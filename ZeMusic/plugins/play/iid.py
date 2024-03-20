import asyncio
from pyrogram import Client, filters
from ZeMusic import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #


iddof = []

@Client.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("♪ الامر معطل من قبل  ⚕️ .")
      iddof.append(message.chat.id)
      return await message.reply_text("♪ تم تعطيل الايدي بنجاح  ⚕️ .")
   else:
      return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  ⚕️ .")

@Client.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id not in iddof:
        return await message.reply_text("♪ الايدي مفعل من قبل  ⚕️ .")
      iddof.remove(message.chat.id)
      return await message.reply_text("♪ تم تفعيل الايدي بنجاح  ⚕️ .")
   else:
      return await message.reply_text("♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  ⚕️ .")

@Client.on_message(filters.command(["ايدي"], "") & filters.group)
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("♪ تم تعطيل امر الايدي من قبل المشرفين  ⚕️ .")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not idd.get(message.from_user.id):
         idd[message.from_user.id] = []
       idd_user = idd[message.from_user.id]
       idd_len = len(idd_user)
       await message.reply_photo(photo=photo, caption=f"name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd_len} 🤍", callback_data=f"heart{user_id}")],]),)
            


idd = {}

@app.on_callback_query(filters.regex("heart") & filters.group)  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in idd.get(usr.id, []):
         idd[usr.id] = []
         idd[usr.id].append(query.from_user.mention)
    else:
         idd[usr.id].remove(query.from_user.mention)
    idd_len = len(idd.get(usr.id, []))
    await query.edit_message_text(f"name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd_len} 🤍", callback_data=f"heart{usr.id}")]]))
  
