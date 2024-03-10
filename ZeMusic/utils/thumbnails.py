import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from youtubesearchpython.__future__ import VideosSearch
from ZeMusic import app
from config import YOUTUBE_IMG_URL

def change_image_size(max_width, max_height, image):
    width_ratio = max_width / image.size[0]
    height_ratio = max_height / image.size[1]
    new_width = int(width_ratio * image.size[0])
    new_height = int(height_ratio * image.size[1])
    new_image = image.resize((new_width, new_height))
    return new_image

async def gen_bot(client, username, photo):
    # Check if the image already exists
    if os.path.isfile(f"{username}.png"):
        return f"{username}.png"

    # Get served users and chats count
    users = len(await get_served_users(client))
    chats = len(await get_served_chats(client))

    # Get thumbnail URL from YouTube video
    url = "https://www.youtube.com/watch?v=gKA2XFkJZhI"
    results = VideosSearch(url, limit=1)
    for result in (await results.next())["result"]:
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]

    # Download and save the thumbnail
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                async with aiofiles.open(f"thumb{username}.png", mode="wb") as f:
                    await f.write(await resp.read())

    # Open images
    youtube = Image.open(f"{photo}")
    mostafa = Image.open(f"{photo}")

    # Resize YouTube image
    resized_youtube = change_image_size(1280, 720, youtube)
    resized_youtube = resized_youtube.convert("RGBA")

    # Apply blur effect to the resized image
    background = resized_youtube.filter(filter=ImageFilter.BoxBlur(5))
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.6)

    # Crop and resize mostafa image
    x_center = mostafa.width / 2
    y_center = mostafa.height / 2
    x1 = x_center - 250
    y1 = y_center - 250
    x2 = x_center + 250
    y2 = y_center + 250
    logo = mostafa.crop((x1, y1, x2, y2))
    logo.thumbnail((520, 520), Image.ANTIALIAS)
    logo = ImageOps.expand(logo, border=15, fill="white")

    # Paste logo onto background
    background.paste(logo, (50, 100))

    # Draw text on the image
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("font2.ttf", 40)
    font2 = ImageFont.truetype("font2.ttf", 70)
    arial = ImageFont.truetype("font2.ttf", 30)

    draw.text((600, 150), "Music Player BoT", fill="white", stroke_width=2, stroke_fill="white", font=font2)
    draw.text((600, 340), "Dev : ALASUOTEY", fill="white", stroke_width=1, stroke_fill="white", font=font)
    draw.text((600, 280), "Playing Music & Video", fill="white", stroke_width=1, stroke_fill="white", font=font)
    draw.text((600, 400), f"user : {users}", (255, 255, 255), font=arial)
    draw.text((600, 450), f"chats : {chats}", (255, 255, 255), font=arial)
    draw.text((600, 500), "Version : 0.1.5", (255, 255, 255), font=arial)
    draw.text((600, 550), f"BoT : t.me\{username}", (255, 255, 255), font=arial)

    # Remove temporary thumbnail file
    try:
        os.remove(f"thumb{username}.png")
    except:
        pass

    # Save the final image
    background.save(f"{username}.png")
    return f"{username}.png"
