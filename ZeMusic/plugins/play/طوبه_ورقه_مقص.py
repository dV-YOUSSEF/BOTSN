import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from typing import Union
from ZeMusic import app
import re
import sys
from pyrogram import Client, filters
from random import choice
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

game_state = {}

options = ["حجرة", "ورقة", "مقص"]

def get_winner(chat_id):
    player1_choice = game_state[chat_id]["player1"]["choice"]
    player2_choice = game_state[chat_id]["player2"]["choice"]
    player1_name = game_state[chat_id]["player1"]["name"]
    player2_name = game_state[chat_id]["player2"]["name"]
    
    if player1_choice == player2_choice:
        return "تعادل"
    elif (player1_choice == "حجرة" and player2_choice == "مقص") or (player1_choice == "ورقة" and player2_choice == "حجرة") or (player1_choice == "مقص" and player2_choice == "ورقة"):
        game_state[chat_id]["player1"]["score"] += 1
        return f"{player1_name}"
    else:
        game_state[chat_id]["player2"]["score"] += 1
        return f"{player2_name}"

app = Client("my_account")

@app.on_message(filters.command("tom"))
def start(client, message):
    if message.chat.id not in game_state:
        game_state[message.chat.id] = {
            "player1": {
                "name": message.from_user.first_name,
                "choice": None,
                "score": 0
            },
            "player2": {
                "name": None,
                "choice": None,
                "score": 0
            }
        }
        message.reply(
            f"{game_state[message.chat.id]['player1']['name']} بدأ لعبة حجرة ورقة مقص.\n\nانتظر اللاعب الثاني...",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اضغط للعب", callback_data="join")],
                    [InlineKeyboardButton("𝙎 .࿆𝙉 .࿆𝙍 </>", url="https://t.me/programer_senzir")]
                ]
            )
        )
    else:
        message.reply("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")

@app.on_callback_query(filters.regex("join"))
def join(client, callback_query):
    if callback_query.message.chat.id in game_state:
        if callback_query.from_user.first_name != game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player2"]["name"] = callback_query.from_user.first_name
            callback_query.message.edit(
                f"{game_state[callback_query.message.chat.id]['player1']['name']} و {game_state[callback_query.message.chat.id]['player2']['name']} يلعبان حجرة ورقة مقص.\n\n👨‍💼 دور اللاعب: {game_state[callback_query.message.chat.id]['player1']['name']}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("𝙎 .࿆𝙉 .࿆𝙍 </>", url="https://t.me/programer_senzir")]
                    ]
                )
            )
        else:
            callback_query.answer("انت منضم للعبه بالفعل", show_alert=True)
    else:
        callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)

@app.on_callback_query(filters.regex("^(حجرة|ورقة|مقص)$"))
def choose(client, callback_query):
    if callback_query.message.chat.id in game_state:
        user_choice = callback_query.data
        bot_choice = choice(options)
        user_name = callback_query.from_user.first_name
        bot_name = client.get_me().first_name

        if user_name == game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player1"]["choice"] = user_choice
            callback_query.message.edit(
                f"👨‍💼 اللاعب الأول: {game_state[callback_query.message.chat.id]['player1']['name']} لقد لعب\n\n👨‍💼 اللاعب الثاني: {game_state[callback_query.message.chat.id]['player2']['name']} اختر الآن...",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("𝐀𝐋𝐏𝐎𝐏", url="https://t.me/V_9_G")]
                    ]
                )
            )
        elif user_name == game_state[callback_query.message.chat.id]["player2"]["name"]:
            if game_state[callback_query.message.chat.id]["player1"]["choice"] is None:
                callback_query.answer("لا يمكنك اللعب حتى يلعب اللاعب الأول.", show_alert=True)
            else:
                game_state[callback_query.message.chat.id]["player2"]["choice"] = user_choice
                winner = get_winner(callback_query.message.chat.id)
                name_player1 = game_state[callback_query.message.chat.id]['player1']['name']
                name_player2 = game_state[callback_query.message.chat.id]['player2']['name']
                choice_player1 = game_state[callback_query.message.chat.id]['player1']['choice']
                choice_player2 = game_state[callback_query.message.chat.id]['player2']['choice']
                player1_score = game_state[callback_query.message.chat.id]['player1']['score']
                player2_score = game_state[callback_query.message.chat.id]['player2']['score']
                callback_query.message.edit(
    f"⌯━─━─━─━──━─━\n"
    f"👨‍💼 {name_player1}: {choice_player1}\n"
    f"👨‍💼 {name_player2}: {choice_player2}\n"
    f"⌯━─━─━─━──━─━\n"
    f"النتيجة:\n"
    f"{winner}!\n"
    f"⌯━─━─━─━──━─━\n"
    f"النقاط:\n"
    f"{name_player1}: {player1_score}\n"
    f"{name_player2}: {player2_score}\n"
    f"⌯━─━─━─━──━─━",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("لعب مرة أخرى", callback_data="join")],
            [InlineKeyboardButton("𝙎 .࿆𝙉 .࿆𝙍 </>", url="https://t.me/programer_senzir")]
        ]
    )
)
