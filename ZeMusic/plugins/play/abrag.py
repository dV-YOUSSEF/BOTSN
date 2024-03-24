import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZeMusic import app
from ZeMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID

@app.on_message(command(["ابراج"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b68edd6cc644f8b661bd6.jpg",
        caption=f"""𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥
\n\n⛥⋮ تنويه هام:- هذا ليس حقيقيا\nـ─────────────────ـ\n⛥⋮ وانما يعلم الغيب سيد الخلائق⁩""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الجدي ›", callback_data="elgadee"),
                    InlineKeyboardButton(
                        "‹ الدلو ›", callback_data="eldaloo"),
                ],[
                    InlineKeyboardButton(
                        "‹ الحوت ›", callback_data="elhout"),
                    InlineKeyboardButton(
                        "‹ الحمل ›", callback_data="elhamal"),
                ],[
                    InlineKeyboardButton(
                        "‹ الثور ›", callback_data="elthawr"),
                    InlineKeyboardButton(
                        "‹ الجوزاء ›", callback_data="elgawzaa"),
                ],[
                    InlineKeyboardButton(
                        "‹ السرطان ›", callback_data="elsaratan"),
                    InlineKeyboardButton(
                        "‹ الاسد ›", callback_data="elaasad"),
                ],[
                    InlineKeyboardButton(
                        "‹ العذراء ›", callback_data="elazraaa"),
                    InlineKeyboardButton(
                        "‹ الميزان ›", callback_data="elmezaan"),
                ],[
                    InlineKeyboardButton(
                        "‹ العقرب ›", callback_data="elaqrab"),
                    InlineKeyboardButton(
                        "‹ القوس ›", callback_data="elqoos"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url="https://t.me/BPHEE"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbahck"))
async def zzzbahck(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥
\n\n⛥⋮ تنويه هام:- هذا ليس حقيقيا\nـ─────────────────ـ\n⛥⋮ وانما يعلم الغيب سيد الخلائق⁩""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ الجدي ›", callback_data="elgadee"),
                    InlineKeyboardButton(
                        "‹ الدلو ›", callback_data="eldaloo"),
                ],[
                    InlineKeyboardButton(
                        "‹ الحوت ›", callback_data="elhout"),
                    InlineKeyboardButton(
                        "‹ الحمل ›", callback_data="elhamal"),
                ],[
                    InlineKeyboardButton(
                        "‹ الثور ›", callback_data="elthawr"),
                    InlineKeyboardButton(
                        "‹ الجوزاء ›", callback_data="elgawzaa"),
                ],[
                    InlineKeyboardButton(
                        "‹ السرطان ›", callback_data="elsaratan"),
                    InlineKeyboardButton(
                        "‹ الاسد ›", callback_data="elaasad"),
                ],[
                    InlineKeyboardButton(
                        "‹ العذراء ›", callback_data="elazraaa"),
                    InlineKeyboardButton(
                        "‹ الميزان ›", callback_data="elmezaan"),
                ],[
                    InlineKeyboardButton(
                        "‹ العقرب ›", callback_data="elaqrab"),
                    InlineKeyboardButton(
                        "‹ القوس ›", callback_data="elqoos"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗡𝗜𝗣𝗘𝗥", url="https://t.me/BPHEE"),
                ],
            ]
       
       ),
    )



@app.on_callback_query(filters.regex("elgadee"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الجدي ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫━━
عاطفيا || 
:  حاول ترطيب الأجواء مع الشريك، بعد ثورة الغضب التي انتابتك في الأيام الماضية 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 لا تنجرّ وراء محاولات استدراجك إلى أن تثور وتغضب لتعريض وضعك الصحي للخطر
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يدعوك هذا اليوم المليء بالسلبيات إلى عدم التورط في قضايا أكبر منك، وخصوصاً أن رياح التغيير بدأت تعصف باتجاهك

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("eldaloo"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الدلو ❫❫━━
مــن :- تاريخ 2024-4-1
꙳.≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫.꙳
عاطفيا || 
:  لا تتسرّع في الموافقة على قرار مهم قبل أن تدرس الوضع من جميع جوانبه، لأن الندم قد لا يفيدك لاحقاً 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 لكي تحافظ على صحتك السليمة، ما عليك سوى ممارسة الرياضة ثلاث مرات على الأقل في الأسبوع
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  هذا اليوم يفرض عليك أن تنظر إلى الأمور بطريقة أخرى، وأن تتعلّم كيف تحوّل الخسارة إلى ربح
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("elhout"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الحوت ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  صداقة قديمة تعود إلى الواجهة عن طريق المصادفة، لكنّ الشريك يشعر بالقلق، فسارع إلى توضيح الأمور 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 لا تستسلم للإحباط بسبب وضعك الصحّي المتردي نوعاً ما، بل كن متسلّحاً بالتفاؤل
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يرّوج بعض الزملاء الإشاعات عن وضعك، لكنّك تبقى صلباً وتحديداً في المركز المهم الذي أسنده إليك أرباب العمل
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("elhamal") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الحمل ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  يحتاج الشريك اليوم إلى عاطفتك واهتمامك أكثر من أي وقت مضى، فاستمع إليه وأمن له ما يتمنّاه 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 القيام ببعض التمارين الخفيفة صباحاً تساعد على تليين العضلات وخصوصاً عضلات العنق الكتفين
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  قد يطرأ اليوم ما يهدد ببعض المشاريع على الصعيد المهني ويكون المناخ ضاغطاً جداً وملبداً بغيوم المشاكل

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("elthawr") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الثور ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  يطلب منك الشريك أن تعطيه جواباً حاسماً بشأن طبيعة العلاقة بينكما، من دون أن يغفل عن أمور تهمكما 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 ترتاح من تعب أرهقك جداً وأبقاك في حالة صحية متذبذبة ومضطربة بعض الشيء
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  حاول ألاّ توظف طاقتك في مشاريع صغيرة لا خطط واضحة لها، وانتظر حتى تعرض عليك المشاريع الكبيرة

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("elgawzaa") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الجوزاء ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  مهمة إقناع الشريك بالسير معك حتى النهاية ليست صعبة، وتجاربه السابقة معك مشجعة جداً 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 أنت المسؤول عما آل إليه وضعك الصحي، لأنك لم تلتزم إرشادات الطبيب ولم تطبقها
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يطرأ اليوم ما يبشر بيوم دقيق من التجارب المرة، لكن النجاح يكون حليفك في نهاية المطاف

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("elsaratan") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
━━❪❪ برج السرطان ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  تمنحك مساندة الحبيب لك في هذه المرحلة الاندفاع والتفاؤل في الحياة والتفكير في الخطوات المقبلة بثقة كبيرة جداً 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 انتبه لصحتك وانظر إلى الخيارات المتاحة أمامك للمحافظة عليها معافاة
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يحمل إليك هذا اليوم كلمات الإطراء والمديح والتهنئة، فيسطع نجمك وتبدأ بمشروع جديد

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzbahck"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("elaasad") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الاسد ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  لا تحمّل الشريك مسؤولية الأخطاء القديمة، وحاول أن تتخطى ذلك برحابة صدر وبساطة 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 التدخين والإفراط في شرب الكحول والسهر سرعان ما تظهر نتائجهما على صحتك
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  قد يجعلك هذا اليوم تتردّد في تسلم مهمة مع أنك تمتلك القدرة على ذلك وتحقيق النجاح المطلوب

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzbahck"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("elazraaa") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج العذراء ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  تشعر بقوة العاطفة وتزداد رغبتك في التقرّب من الشريك الذي تكنّ له الحب الكبير 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 إذا أحسست أن وضعك الصحي يتحسّن، فهذا جراء تطبيق إرشادات أصحاب الاختصاص في مجال التغذية
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يولّد هذا اليوم كلاماً غير مقنع أو لا يتمتّع بمصداقية، فتحاول معرفة الأسباب الكامنة وراء كل ما يحصل وتنجح في ذلك

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzbahck"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("elmezaan") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج الميزان ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  تمرّ بظرف صعب اليوم وأنت بأمسّ الحاجة إلى مساندة الشريك لتجاوز ما تواجهه بأقل ضرر ممكن 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 تنضم إلى إحدى الفرق أو المجموعات الرياضية وتواظب على المشاركة في جميع أنشطتها فتستفيد صحياً
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  يجعلك هذا اليوم تشغل نفسك بأمور صغيرة لن تنفعك بشيء، بل بالعكس قد تضيّع لك وقتك، وأنت بحاجة ماسة إلى كل ثانية

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("elaqrab") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج العقرب ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  كثرة التأجيل في حسم الأمور المصيرية تهدد علاقتك بالشريك، وتدفعها إلى المزيد من التأزم 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 قد تشعر بضيق في النفس وباضطراب مفاجئ في الرئتين بسبب إدمانك التدخين
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  قد يعرقل طارئ هذا اليوم تقدمك في مجالك المهني، لكنك قادر على تخطي المصاعب مهما تكن شديدة

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("elqoos") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⭓ ᴍᴜˢɪᴄ ⭓
       
━━❪❪ برج القوس ❫❫━━
مــن :- تاريخ 2024-4-1
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
عاطفيا || 
:  كن طويل البال مع الشريك وامنحه مزيداً من الوقت، فهو ساعدك كثيراً ويستحق منك بعض التضحية 
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
صحياً ||
 تجنّب قدر الإمكان الأماكن الرطبة ولا سيما أنك تعاني الربو وضيقاً في التنفس
≪━━━━𝘴ꪮꪊ𝘳ᥴꫀ 𝘴ꪀipꫀ𝘳━━━━≫
مهنياً ||
  قد يفقدك هذا اليوم الظروف المشجعة على التحرّك والاستثمار وتوظيف الأموال وتحقيق الأرباح

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzbahck"),
               ],
          ]
        ),
    )
