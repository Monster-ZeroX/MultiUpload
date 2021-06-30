import asyncio, json, os
from multiupload import anjana
from telethon.sync import events
from datetime import datetime
import time
from multiupload.utils import humanbytes, progress, time_formatter, download_file
from config import LOG_CHANNEL

@anjana.on(events.NewMessage(pattern='/ufile'))
async def ufile(e):
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
	await asyncio.sleep(2)

	await snd.edit('Creating Session')
	await asyncio.sleep(1)
	try:
		anonul = await asyncio.create_subprocess_shell(f"""curl 'https://up.ufile.io/v1/upload/create_session' \
  -d 'file_size={os.path.getsize(file_path)}'""", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		kek = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"ERR: {err}")
	fuid = kek["fuid"]


	await snd.edit('Creating Chunk')
	await asyncio.sleep(1)
	try:
		anonul = await asyncio.create_subprocess_shell(f"""curl 'https://up.ufile.io/v1/upload/chunk' \
  -F 'chunk_index=1' \
  -F 'fuid={fuid}' \
  -F 'file=@{file_path}'""", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		kek = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"ERR: {err}")

	root, extension = os.path.splitext(file_path)


	await snd.edit('Uploading to UFile')
	await asyncio.sleep(1)
	try:
		anonul = await asyncio.create_subprocess_shell(f"""curl 'https://up.ufile.io/v1/upload/finalise' \
  -d 'fuid={fuid}' \
  -d 'file_name={root}' \
  -d 'file_type={extension.replace(".", "")}' \
  -d 'total_chunks=1'""", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
		kek = json.loads(stdout)
	except Exception as err:
		return await snd.edit(f"ERR: {err}")


	dlurl = kek["url"]
	filesiz = kek["size"]
	filname = file_path
	hmm = f'''File Uploaded successfully !!
Server: UFile

**~ File name** = __{filname}__
**~ File size** = __{filesiz}__
**~ Download Link**: __{dlurl}__'''
	await snd.edit(hmm)

	## LOGGING TO A CHANNEL
	xx = await e.get_chat()
	reqmsg = f'''Req User: <a href="tg://user?id={xx.id}">{xx.first_name}</a>
FileName: {filname}
FileSize: {filesiz}
#UFILE'''
	await anjana.send_message(LOG_CHANNEL, reqmsg)
	os.remove(file_path)