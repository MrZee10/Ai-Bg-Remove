from pyrogram import Client
from pyrogram.types import filters
from config import config


@Client.on_message(filters.photo())
async def removebg_plain(client, message):
    try:
        if not (Config.RemoveBG_API == ""):
            userid = str(message.chat.id)
            if not os.path.isdir(f"./DOWNLOADS/{userid}"):
                os.makedirs(f"./DOWNLOADS/{userid}")
            download_location = "./DOWNLOADS" + "/" + userid + "/" + userid + ".jpg"
            edit_img_loc = "./DOWNLOADS" + "/" + userid + "/" + "nobgplain.png"
            if not message.reply_to_message.empty:
                msg = await message.reply_to_message.reply_text(
                    "<b>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>", quote=True
                )
                await client.download_media(
                    message=message.reply_to_message, file_name=download_location
                )
                await msg.edit("<b>𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙸𝙼𝙰𝙶𝙴....</b>")

                response = requests.post(
                    "https://api.remove.bg/v1.0/removebg",
                    files={"image_file": open(download_location, "rb")},
                    data={"size": "auto"},
                    headers={"X-Api-Key": Config.RemoveBG_API},
                )
                if response.status_code == 200:
                    with open(f"{edit_img_loc}", "wb") as out:
                        out.write(response.content)
                else:
                    await message.reply_to_message.reply_text(
                        "Check if your api is correct", quote=True
                    )
                    return

                await message.reply_chat_action("upload_document")
                await message.reply_to_message.reply_document(edit_img_loc, quote=True)
                await msg.delete()
            else:
                await message.reply_text("Why did you delete that??")
            try:
                shutil.rmtree(f"./DOWNLOADS/{userid}")
            except Exception:
                pass
        else:
            await message.reply_to_message.reply_text(
                "Get the api from https://www.remove.bg/b/background-removal-api and add in Config Var",
                quote=True,
                disable_web_page_preview=True,
            )
    except Exception as e:
        print("removebg_plain-error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_to_message.reply_text(
                    "Something went wrong!", quote=True
                )
            except Exception:
                return
