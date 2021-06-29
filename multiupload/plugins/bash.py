import os
from multiupload import anjana
from telethon import events

@anjana.on(events.NewMessage(pattern='/bash'))
async def bash(e):
	xx = await e.get_chat()
	if xx.id == 1252058587:
		pass
	else:
		print(xx.first_name + " trying to excute a cmd")
		return await anjana.send_message(e.chat_id, "You are not a Developer")

	cmd = await event.get_reply_message()
	shell = await asyncio.create_subprocess_shell(f"{cmd}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
	stdout, strderr = await shell.communicate()

	await anjana.send_message(e.chat_id, stdout)