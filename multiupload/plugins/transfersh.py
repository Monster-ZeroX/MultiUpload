import asyncio, json, os
from multiupload import anjana
from telethon.sync import events

@anjana.on(events.NewMessage(pattern='/tsh'))
async def tsh(e):
	amjana = await e.get_reply_message()
	pamka = "./downloads/"
	noize = amjana.file.name
	snd = await anjana.send_message(e.chat_id, 'Start Downloading')
	file_name = await anjana.download_media(amjana, pamka)
	path = pamka+noize
	await snd.edit('Success !!\n Path: '+path)
	await asyncio.sleep(3)

	await snd.edit('Now uploading to Transfer.SH')
	try:
		anonul = await asyncio.create_subprocess_shell(f"curl --upload-file {path} https://transfer.sh/{noize}", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
		stdout, strderr = await anonul.communicate()
	except Exception as err:
		return await snd.edit(f"`ERR: {err}`")

	filesiz = os.path.getsize(path)
	hmm = f'''File Uploaded successfully !!
**File name** = __{noize}__
**File size** = __{filesiz}__

**Download Link**: __{stdout}__'''
	await snd.edit(hmm)
	os.remove(f'{path}')   
	os.system("cd downloads && ls")