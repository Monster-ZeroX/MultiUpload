import asyncio
import io
import os
import sys
import traceback
from multiupload import anjana
from telethon import events

@anjana.on(events.NewMessage(pattern='/bash'))
async def bash(event):
    kk = await event.get_chat()
    if kk.id == 1252058587:
        pass
    else:
        return await anjana.send_message(event.chat_id, "You are not a Developer")

    cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    catevent = await anjana.send_message(event.chat_id, "Executing.....")
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    curruser = "AnjanaMa"
    uid = os.geteuid()
    if uid == 0:
        cresult = f"**{curruser}:~# {cmd}**\n{result}"
    else:
        cresult = f"**{curruser}:~$ {cmd}**\n{result}"
    await catevent.edit(cresult)