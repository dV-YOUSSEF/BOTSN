import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from strings.filters import command
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from ZeMusic import app

# ------------------------------------------------------------------------------- #

chatQueue = []

stopProcess = False

# ------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------- #

@app.on_message(command(["/admins","الادمن","الادمنيه"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**مجموعة ستافي - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 ᴏᴡɴᴇʀ\n└ {owner.mention}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
      else:
        text2 += f"👑 ᴏᴡɴᴇʀ\n└ @{owner.username}\n\n👮🏻 ᴀᴅᴍɪɴs\n"
    except:
      text2 += f"👑 ᴏᴡɴᴇʀ\n└ <i>Hidden</i>\n\n👮🏻 ᴀᴅᴍɪɴs\n"
    if len(adminList) == 0:
      text2 += "└ <i>ᴀᴅᴍɪɴs ᴀʀᴇ ʜɪᴅᴅᴇɴ</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"**✅ | العدد الإجمالي للمسؤولين: {lenAdminList}**"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

# ------------------------------------------------------------------------------- #

@app.on_message(command(["bots","بوتات","/bots","البوتات","عدد البوتات"]))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"**قائمة البوتات - {message.chat.title}\n\n🤖 البوتات\n**"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"**✅ | مركز تجاري للبوتات: 1 {lenBotList}**"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
    
# ------------------------------------------------------------------------------- #

