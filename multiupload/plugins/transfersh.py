from multiupload import anjana
import asyncio
import datetime
import os
import time
import aiohttp
from telethon import events

from multiupload.utils import humanbytes, progress, download_file
from config import LOG_CHANNEL

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
        pass
    else:
        return await anjana.send_message(event.chat_id, "Please Reply to File")

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
        await snd.edit(f"Downloading Failed\n\n<b>Error:</b> {e}")

    try:
        await snd.edit("Uploading to TransferSh...")
        download_link, size = await send_to_transfersh_async(file_path)

        str(time.time() - start)
        kl = humanbytes(os.path.getsize(file_path))
        hmm = f'''File Uploaded successfully !!
Server: TransferSH

<b>~ File name</b> = <i>{url.file.name}</i>
<b>~ File size</b> = <i>{kl}</i>
<b>~ Download Link</b>: <i>{download_link}</i>'''
        await snd.edit(hmm)
    except Exception as e:
        await snd.edit(f"Uploading Failed\n\n<b>Error:</b> {e}")

    ## LOGGING TO A CHANNEL
    xx = await event.get_chat()
    reqmsg = f'''Req User: <a href="tg://user?id={xx.id}">{xx.first_name}</a>
FileName: {url.file.name}
FileSize: {kl}
#TRANSFERSH'''
    await anjana.send_message(LOG_CHANNEL, reqmsg)
    os.remove(file_path)

    raise events.StopPropagation