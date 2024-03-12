import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

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

@app.on_message(filters.command(["start"], "") & filters.private & ~BANNED_USERS)
async def madison(client: Client, message: Message): 
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

@app.on_message(filters.command(["ꨄ حذف الكيبورد ꨄ"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command("⛔ ¦ المحظورين") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/89840a4c57675832debf9.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🍁 ¦ حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5dc0bab3462bd868b3081.jpg",
        caption=f"""• اليك طريقه حظر اي شخص .\n\n• قم بـ استخدام الامر هكذا : /block حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🖇 ¦ الغاء حظر") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4268ef332d710c5547357.jpg",
        caption=f"""• اليك طريقه الغاء حظر شخص .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔥 ¦ المحظورين عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cc2b0b6c4eea77c43b8b4.jpg",
        caption=f"""• اليك طريقه معرفه المحظورين عام .\n\n• قم بـ استخدام الامر هكذا : /blockedusers المحظورين ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🗞 ¦ حظر عام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d0db8351713f77bb8450b.jpg",
        caption=f"""• اليك طريقه الحظر العام .\n\n• قم بـ استخدام الامر هكذا :/ح ع\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🔖 ¦ الغاء العام") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/611ee77edc1763ea2b07b.jpg",
        caption=f"""• اليك طريقه الغاء الحظر العام .\n\n• قم بـ استخدام الامر هكذا : /unblock الغاء حظر ميوزك\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command("🪂 ¦ الاحصائيات") & filters.private & filters.group)
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/571e1fb1857c8ae6e6be1.jpg",
        caption=f"""• اليك طريقه معرفه الاحصائيات .\n\n• قم بـ استخدام الامر هكذا : الاحصائيات\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )

@app.on_message(filters.command(["ذكاء الاصطناعي"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c544b771eeed7dbdc51a9.jpg",
        caption=f"""• اليك طريقه معرفه سرعه البوت .\n\n• قم بـ استخدام الامر هكذا : /gpt\n\n• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ » @AlmortagelTech .\n•⊶⊶★─⊶『[Almortagel](https://t.me/AlmortagelTech)』⊶⊶★─⊶•""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ .", url=f"https://t.me/AlmortagelTech"),
            ],
            ]
        ),
    )
