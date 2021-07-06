import asyncio, random
from telethon import events, Button
from multiupload.fsub import *
from multiupload import anjana

s = ["CAADBAADxgkAAjQF0VL5yl4Td0utTgI",
	"CAADBAADoAsAAv3iYFGE3u_w4y_1zgI",
	"CAADBAADMggAAq0Q0FK1ZIUPLNxGcAI",
	"CAADBAAD7AoAAr8i2VGALarwosnJIgI",
	"CAADBAADrQoAAmzO0VFDq1aGz7rGHgI",
	"CAADBAADbQgAAhI40VH51AABGZuwl74C"]

@anjana.on(events.NewMessage(pattern='^/start'))
async def start(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, '@harp_tech', event):
		return
	else:
		await anjana.send_file(event.chat_id, random.choice(s), reply_to=event)
		await event.reply(f"Hey [{xx.first_name}]({xx.id}), I am **MultiUploader**", buttons=[
				Button.url('Support Chat 💭', 't.me/harp_chat')
			])


@anjana.on(events.NewMessage(pattern='^/help'))
async def help(event):
	async with anjana.action(event.chat_id, 'typing'):
		await asyncio.sleep(3)
	user_id = event.sender_id
	xx = await event.get_chat()
	if event.is_private and not await check_participant(user_id, '@harp_tech', event):
		return
	else:
		helpmsg = '''
➖ **Help Menu | MultiUpload** ➖
● `/gofile` - Upload files to GoFile
● `/anonfile` - Upload files to AnonFile
● `/ufile` - Upload files to UFile
● `/bayfiles` - Upload files to BayFiles
● `/tsh` - Upload files to TransferSH
● `/tninja` - Upload files to TmNinja
● `/fileio` - Upload files to FileIO
● `/mixdrop` - Upload files to MixDrop

✦ **Powered By [Harp Tech]**(t.me/harp_tech)
✦ Made with ♥️ by [Anjana](t.me/anjana_ma)'''
		await event.reply(helpmsg, buttons=[
				Button.url('Support Chat 💭', 't.me/harp_chat')
			], link_preview=False)