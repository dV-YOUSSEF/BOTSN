import asyncio
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from pyrogram.types import User

REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"

REPLY_MESSAGE_BUTTONS = [
    [
        ("• السورس •"),
    ],
    [
        ("• المطور •"),
        ("• مطور السورس •"),
    ],
    [
        ("• تويت •"),
        ("• صراحه •"),
    ],
    [
        ("• معلومات دينيه •"),
    ],
    [
        ("كسمك😂"),
        ("• امثله •"),
    ],
    [
        ("• نكته •"),
        ("• فزوره •"),
    ],
    [
        ("• المختلف •"),
    ],
    [
        ("• اعلام •"),
        ("• تفكيك •"),
    ],
    [
        ("• رمزيه •"),
        ("• صور •"),
    ],
    [
        ("• عقاب •"),
        ("• تحدي •"),
    ],
    [
        ("• لو خيروك •"),
    ],
    [
        ("ꨄ حذف الكيبورد ꨄ"),
    ]
]

app = Client("my_account")

# معرف المطور للبوت
BOT_DEVELOPER_ID = 6943111120  # قم بتغيير هذا بمعرف مطور البوت الفعلي

# دالة للتحقق مما إذا كان المستخدم مطور البوت
def is_bot_developer(user: User) -> bool:
    return user.id == BOT_DEVELOPER_ID

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
    text = REPLY_MESSAGE
    # التحقق مما إذا كان المستخدم مطور البوت أو لا
    if is_bot_developer(message.from_user):
        # إذا كان مطور البوت، استخدم الكيبورد المطور
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
    else:
        # إذا لم يكن مطور البوت، استخدم الكيبورد العادي
        reply_markup = None
    await message.reply(
        text=text,
        reply_markup=reply_markup
    )

@app.on_message(filters.regex("hide buttons"))
async def hide_buttons(client, message):
    await message.delete()

@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_youtube(Client, message):
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

app.run()
