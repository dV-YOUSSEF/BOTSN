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


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"


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

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**تم قفل الكيبورد بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url=f"https://t.me/BPHEE"),
            ]
         ]
     )
  )

