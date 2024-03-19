import asyncio
from pyrogram import Client, filters
from strings.filters import command
from ZeMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "<b>صلي علي النبي وتبسم ♥️✨</b>"

REPLY_MESSAGE_BUTTONS = [
    [
             ("• السورس •")

          ],
          [
             ("• المطور •"),
             ("• مطور السورس •")
          ],
          [
             ("• تويت •"),
             ("• صراحه •") 
          ],
          [
             ("• معلومات دينيه •") 
          ],
          [
             ("• اسئله •"),
             ("• امثله •") 
          ],
          [
             ("• نكته •"),
             ("• فزوره •")
          ],
          [
             ("• المختلف •")
          ],
          [
              ("• اعلام •"),
              ("• تفكيك •")
          ],
          [
             ("• رمزيه •"),
             ("• صور •")         
          ],
          [
             ("• عقاب •"),
             ("• تحدي •")
          ],
          [
             ("• لو خيروك •")
          ],
          [           
        ("ꨄ حذف الكيبورد ꨄ")
    ]
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("ꨄ حذف الكيبورد ꨄ"))
async def down(client, message):
          m = await message.reply("ꨄ تـم حذف الكيبورد ꨄ", reply_markup= ReplyKeyboardRemove(selective=True))

