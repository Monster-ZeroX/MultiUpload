import asyncio, json, os
from multiupload import anjana
from telethon.sync import events
from datetime import datetime
import time
from multiupload.utils import humanbytes, progress, time_formatter, download_file

@anjana.on(events.NewMessage(pattern='/gofile'))
async def gofile(e):
	if e.reply_to_msg_id:
		pass
	else:
		return await anjana.send_message(e.chat_id, "Please Reply to File")

	amjana = await e.get_reply_message()
	pamka = "./downloads/"
	noize = amjana.file.name
	k = time.time()
	snd = await anjana.send_message(e.chat_id, 'Start Downloading')


	try:
		file_path = await amjana.download_media(
			progress_callback=lambda pamka, t: asyncio.get_event_loop().create_task(
				progress(pamka, t, snd, k, "Downloading...")
			)
		)
	except Exception as e:
		await snd.edit(f"Downloading Failed\n\n**Error:** {e}")


	await snd.edit('Success !!\n Path: '+file_path)
	await asyncio.sleep(3)

	await snd.edit('Getting Server...')
	await asyncio.sleep(1)
	try:
		anonul = await asyncio.create_subprocess_shell("curl https://api.gofile.io/getServer", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		srfl = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"`ERR: {err}`")
	servr = srfl["data"]["server"]


	await snd.edit('Uploading to GoFile')
	try:
		anonul = await asyncio.create_subprocess_shell(f"curl -F file=@{file_path} https://{servr}.gofile.io/uploadFile", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		kek = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"`ERR: {err}`")


	dlurl = kek["data"]["downloadPage"]
	filesiz = humanbytes(os.path.getsize(file_path))
	filname = kek["data"]["fileName"]
	hmm = f'''File Uploaded successfully !!
Server: GoFile

**~ File name** = __{filname}__
**~ File size** = __{filesiz}__
**~ Download Link**: __{dlurl}__'''

	await snd.edit(hmm)
	os.remove('downloads/'+file_path)

	## LOGGING TO A CHANNEL
    xx = await e.get_chat()
    reqmsg = f'''Req User: [{xx.first_name}](tg://user?id={xx.id})
FileName: {filname}
FileSize: {filesiz}
#GOFILE'''
    await anjana.send_message(LOG_CHANNEL, reqmsg)