import os
import future
import asyncio
import requests
import time
import yt_dlp
from urllib.parse import urlparse
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from strings.filters import command
from ZeMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command(["yt", "video"]))
async def ytmusic(client, message: Message):
    urlissed = get_text(message)
    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, f"**╮جـار تحــمـيل فــيديو... 🎧♥️╰**")
    if not urlissed:
        await pablo.edit(
            "**عـايـز تــنزل اي....🥺💚🍀**"
        )
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            round(infoo["duration"] / 60)
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**شکستی ‌هێنا لە داگرتن\nهەڵە :** `{str(e)}`")
        return
    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**ناونیشان : [{thum}]({mo})\n\nکەناڵ : {thums}\nگەڕان : {urlissed}\nلەلایەن : {chutiya}**"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress_args=(
            pablo,
            c_time,
            f"**❈╎لە ھہێنَِٰہآنَِٰہ دُآیە کەمـێڪٰྀہٰٰٖ چآوًەڕێ بّہکە.⏳🧡:)**\n\n**دٰاٰدٰەبـٰ̲ـہەزٰێتـٰ̲ـہ!🥀🎼 ، ⇣** `{urlissed}` **لە سێرڤەری یوتوب**",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


# ------------------------------------------------------------------------------- #

@app.on_message(command(["/song", "/search", "نزل", "تحميل", "حمل", "يوتيوب"]))
def download_song(_, message):
    query = " ".join(message.command[1:])
    print(query)
    m = message.reply("**╮جـار تحــمـيل مـوسـيقي... 🎧♥️╰**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results[0]["views"]
        channel_name = results[0]["channel"]

    except Exception as e:
        m.edit("**عـايـز تــنزل اي....🥺💚🍀**")
        print(str(e))
        return
    m.edit("**❈╎لە ھہێنَِٰہآنَِٰہ دُآیە کەمـێڪٰྀہٰٰٖ چآوًەڕێ بّہکە.⏳🧡:)**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**دٰاٰدٰەبـٰ̲ـہەزٰێتـٰ̲ـہ!🥀🎼 ، ⇣**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            duration=dur,
            caption=f"**{title}\n\nلەلایەن ➪ {message.from_user.mention}\nبینەر ➪ {views}\nکەناڵ ➪ {channel_name}**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "𝚈𝙾𝚄𝚃𝚄𝙱𝙴", url=f"https://youtube.com{results[0]['url_suffix']}"
                        )
                    ],
                ]
            ),
        )
        m.delete()
    except Exception as e:
        m.edit("**هەڵە ڕوویدا**")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


