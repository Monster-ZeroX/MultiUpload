from multiupload import anjana
import asyncio
import datetime
import os
import time
import aiohttp
from telethon import events

from multiupload.utils import humanbytes, progress, download_file

async def send_to_transfersh_async(file):

    size = os.path.getsize(file)
    size_of_file = humanbytes(size)
    file_name = os.path.basename(file)

    print("\nUploading file: {} (size of the file: {})".format(file_name, size_of_file))
    url = "https://transfer.sh/"

    with open(file, "rb") as f:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data={str(file): f}) as response:
                download_link = await response.text()

    return download_link, size_of_file


@anjana.on(events.NewMessage(pattern="/transfersh"))
async def tsh(event):
    if event.reply_to_msg_id:

        start = time.time()
        url = await event.get_reply_message()
        snd = await anjana.send_message(event.chat_id, "Starting Download...")
        d = "./downloads"
        try:
            file_path = await url.download_media(
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, snd, start, "Downloading...")
                )
            )
        except Exception as e:
            await snd.edit(f"Downloading Failed\n\n**Error:** {e}")

        try:
            await snd.edit("Uploading to TransferSh...")
            download_link, size = await send_to_transfersh_async(file_path)

            str(time.time() - start)
            hmm = f'''File Uploaded successfully !!
**File name** = __{file_name}__
**File size** = __{size_of_file}__

**Download Link**: __{download_link}__'''
            await snd.edit(hmm)
        except Exception as e:
            await snd.edit(f"Uploading Failed\n\n**Error:** {e}")

    raise events.StopPropagation
