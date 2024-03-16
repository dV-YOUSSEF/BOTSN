from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import OWNER_ID, BANNED_USERS

# تحديد الرسالة التي ستُرسل في حالة الرد على الأمر "start"
REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"

# تحديد الأزرار التي ستظهر في الكيبورد
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
        ("• 🤍​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​🌝 •") 
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
        ("• 💚​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​🌝 •")
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

# دالة لفتح الكيبورد عند الأمر "start"
@app.on_message(filters.command(["start"], "") & filters.private & ~BANNED_USERS)
async def madison(client: Client, message: Message): 
    # التحقق مما إذا كان المرسل مطور البوت
    if message.from_user.id == DEVELOPER_ID:
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
        await message.reply(
            text=text,
            reply_markup=reply_markup
        )

# دالة لحذف الكيبورد
@app.on_message(filters.command(["ꨄ حذف الكيبورد ꨄ"], "") & filters.user(DEVELOPER_ID))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

# بدء تشغيل البوت
app.run()
