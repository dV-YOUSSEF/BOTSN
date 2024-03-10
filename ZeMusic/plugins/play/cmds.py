import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID

@app.on_message(command(["اوامر", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b68edd6cc644f8b661bd6.jpg",
        caption=f"""⌔︙اوامــر البــوت الرئيسيـة \n—————————————\n⌔︙اختر ماتريد عرضه من القائمه :\n\nقناه السورس :𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥
—————————————""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الحمايه م1", callback_data="zzzll"),
                    InlineKeyboardButton(
                        "اوامر الادمنيه م2", callback_data="zzzzzad"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المدراء م3", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "اوامر المنشئين م4", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المالكيـن م5", callback_data="youssef"),
                    InlineKeyboardButton(
                        "اوامر التحشيش م6", callback_data="zyiusse"),
                ],[
                    InlineKeyboardButton(
                        "اوامــر التسليـه م7", callback_data="zzyiudgk"),
                    InlineKeyboardButton(
                        "اوامــر البنـــك م8", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المطـور م", callback_data="zzyiudgk"),
                    InlineKeyboardButton(
                        "اوامـر التـشغيل", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "الالـعــاب", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "القفل / الفتح", callback_data="zzzdv"),
                    InlineKeyboardButton(
                        "التفعيل/ التعطيل", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url="https://t.me/BPHEE"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""⌔︙اوامــر البــوت الرئيسيـة \n—————————————\n⌔︙اختر ماتريد عرضه من القائمه :\n\nقناه السورس :𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥
—————————————""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الحمايه م1", callback_data="zzzll"),
                    InlineKeyboardButton(
                        "اوامر الادمنيه م2", callback_data="zzzzzad"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المدراء م3", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "اوامر المنشئين م4", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المالكيـن م5", callback_data="youssef"),
                    InlineKeyboardButton(
                        "اوامر التحشيش م6", callback_data="zyiusse"),
                ],[
                    InlineKeyboardButton(
                        "اوامــر التسليـه م7", callback_data="zzyiudgk"),
                    InlineKeyboardButton(
                        "اوامــر البنـــك م8", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المطـور م", callback_data="zzyiudgk"),
                    InlineKeyboardButton(
                        "اوامـر التـشغيل", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "الالـعــاب", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "القفل / الفتح", callback_data="zzzdv"),
                    InlineKeyboardButton(
                        "التفعيل/ التعطيل", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url="https://t.me/BPHEE"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>↯︙مرحباً بك عزيزي المطور </b>\n\n<b>↯︙استخدم الازرار بالاسفل\n↯︙ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ التحديث ›", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "‹ الرفع ›", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "‹ الحظر ›", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "‹ اشعارات & المساعد ›", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzyiudgk"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⛥━━━━━( اوامر التشغيل )━━━━━⛥

( تشغيل او شغل ) + ( اسم الاغنيه او جزا اي الاغنيه )

⛥━━━━━( ملحوظه هامه )━━━━⛥

( البوت يعمل في الجروبات والقنوات ) ( بنفس الاوامر )

⛥━━━━( نتمني فرحكتم  )━━━━━⛥</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⛥━━━━━━( اوامر الادمن )━━━━━━⛥

( هذه الاوامر خاصه بلامن فقط ويمكن تعدلها للجميع )

⛥━━━━━━( اوامر التخطي )━━━━━━⛥

(تخطي او التالي ) (عشان تتخطي الاغنيه )

⛥━━━━( اوامر الوقوف المؤقت )━━━━━⛥

( وقف ) ( لإيقاف الاغنيه مؤقتا )

⛥━━━━━( اوامر الاستثناء )━━━━━━⛥

( كمل ) ( لتكمله الاغنيه اللي شغاله )

⛥━━━━━━( اوامر الايقاف )━━━━━━⛥

( ايقاف ) ( لإيقاف الاغنيه اللي شغاله في الكول )

⛥━━━━━( نتمني فرحكتم  )━━━━━━⛥</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر التشغيل في القناة :</b>
– – – – – – – – – – – – – – – – – –
<b>- ارفع البوت إشراف في القناة و شغل مباشر</b>
<b>- ارسل (/channelplay او ربط) + يوزر القناة ل الربط</b>
<b>- ثم استخدم الاوامر بالاسفل ل التشغيل</b>
– – – – – – – – – – – – – – – – – –
تشغيل + اسم الاغنية
<b>- ل تشغيل اغنية في المكالمة الصوتية</b>
– – – – – – – – – – – – – – – – – –
فيديو + اسم المقطع
<b>- ل تشغيل فيديو في المكالمة المرئية</b>
– – – – – – – – – – – – – – – – – –
ايقاف / انهاء / اسكت
<b>- ل إيقاف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
وقف / توقف
<b>- ل إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</b>
– – – – – – – – – – – – – – – – – –
كمل / استئناف
<b>- ل إستئناف تشغيل الموسيقى في المكالمة</b>
– – – – – – – – – – – – – – – – – –
تخطي
<b>- ل تخطي الاغنية وتشغيل الاغنية التاليه</b>
– – – – – – – – – – – – – – – – – –
/seek + عدد الثواني
<b>- ل تقديم الاغنيه ل الامام</b>
/seekback + عدد الثواني
<b>- ل إرجاع الاغنيه ل الخلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر التحديثات :</b>
– – – – – – – – – – – – – – – – – –
السجلات
<b>- لـ جلب سجلات البوت</b>
– – – – – – – – – – – – – – – – – –
تحديث
<b>- لـ تحديث البوت</b>
– – – – – – – – – – – – – – – – – –
اعاده تشغيل
<b>- لـ اعادة تشغيل البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الحظر :</b>
– – – – – – – – – – – – – – – – – –
بلوك/الغاء بلوك/المبلكين
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
احظره عام/الغاء حظره عام
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت عام</b>
– – – – – – – – – – – – – – – – – –
المحظورين عام
<b>- ل جلب قائمة المحظورين عام في البوت</b>
– – – – – – – – – – – – – – – – – –
حظر مجموعة/سماح
<b>- ل حظر/الغاء حظر مجموعة من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المجموعات المحظورة
<b>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>↯︙قائمة اوامر المساعد :</b>
– – – – – – – – – – – – – – – – – –
السجل ⦗ تفعيل / تعطيل ⦘
<b>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</b>
– – – – – – – – – – – – – – – – – –
⦗ المغادره التلقائيه ⦗ تفعيل / تعطيل
<b>- ل تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم استخدام الميوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("zzyius") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⩹━⛥━𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥━★━⩺
       
اوامر القفل و الفتح للحمايه:

╮ ⇐الصور
│──────────────────
│⇐  الروابط
│──────────────────
│⇐  السب
│──────────────────
│⇐  التوجيه
│──────────────────
│⇐  الفيديو
│──────────────────
│⇐  التثبيت 
│──────────────────
│⇐  الكل
│──────────────────
│⇐  الملصقات
│──────────────────
│⇐  الايدي
│──────────────────
│⇐  جمالي
│──────────────────
│⇐  الحظر
│──────────────────
│⇐  الكتم
│──────────────────
│⇐ البايو
│──────────────────
│⇐ الدعوه
│──────────────────
│⇐ المتحركات
│──────────────────
│⇐ الاباحي
│──────────────────
╯ ⇐ التقيد
⩹━⛥━𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥━★━⩺

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("zyiusse") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
اوامر الحمايه 

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("youssef") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗣𝗢𝗣⌝━⊶★━⩺

★¦العاب مارو
★¦كت
★¦تويت
★¦اسال
★¦اصراحه

⩹━★⊷━⌞𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗣𝗢𝗣⌝━⊶★━⩺.

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_message(command(["مطور", "المطور"]) & filters.group)
async def zilzal(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    async for photo in client.iter_profile_photos(OWNER_ID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ٴ<b>- - - - - - - - - - - - - - - - - -</b>
                    
- 𝚆𝙾𝙽𝙴𝚁 :{usr.first_name}
- 𝚄𝚂𝙴𝚁 :@{usrnam} 
- 𝙸𝙳 :{usr.id}
 </b>- - - - - - - - - - - - - - - - - -</b> """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{usrnam}"),
            ],[
              InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗔𝗟𝗣𝗢𝗣", url="https://t.me/source_alpop"),
            ],
          ]
       )                 
    )                    
                    sender_user = "@{senderuser}" if senderuser else "لا يوجـد"
                    await app.send_message(OWNER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
                    return await app.send_message(LOGGER_ID, f"- المستخـدم {message.from_user.mention} يناديـك \n\n- الاسـم : {sender_name} \n- الايـدي : {sender_id}\n- اليـوزر : {sender_user}")
