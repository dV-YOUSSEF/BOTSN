from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت اللي مجموعتك 💚.", url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضف البوت اللي مجموعتك 💚.",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="**طريقة التشغيل**", callback_data="kdkdklodas"),
            InlineKeyboardButton(text="**طريقة التفعيل**", callback_data="kdkdodas"),
        ],
        [
            InlineKeyboardButton(text="الجروب", url=f"https://t.me/B_X_N1"),
            InlineKeyboardButton(text="القناة", url=f"https://t.me/BPHEE"),
        ],
        [
            InlineKeyboardButton(text="𝗬.𝗢.𝗨.𝗦.𝗦.𝗘.𝐅", user_id=config.OWNER_ID),
        ],
    ]
    return buttons
