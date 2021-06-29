import asyncio, json, os
from multiupload import anjana
from telethon.sync import events
from datetime import datetime
import time
from multiupload.utils import humanbytes, progress, time_formatter, download_file

@anjana.on(events.NewMessage(pattern='/anonfile'))
async def anonfile(e):
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

	await snd.edit('Now uploading to AnonFile')


	try:
		anonul = await asyncio.create_subprocess_shell("curl -F 'file=@"+file_path+"' https://api.anonfiles.com/upload", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		kek = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"`ERR: {err}`")


	dlurl = kek["data"]["file"]["url"]["full"]
	filesiz = kek["data"]["file"]["metadata"]["size"]["readable"]
	filname = kek["data"]["file"]["metadata"]["name"]
	hmm = f'''File Uploaded successfully !!
**File name** = __{filname}__
**File size** = __{filesiz}__

**Download Link**: __{dlurl}__'''


	await snd.edit(hmm)
	os.remove(f'{file_path}')   
	os.system("cd downloads && ls")