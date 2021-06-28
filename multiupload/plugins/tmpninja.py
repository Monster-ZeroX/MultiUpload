import asyncio, json, os, requests
from multiupload import anjana
from telethon.sync import events

@anjana.on(events.NewMessage(pattern='/tmpninja'))
async def tmpninja(e):
	amjana = await e.get_reply_message()
	pamka = "./downloads/"
	noize = amjana.file.name
	snd = await anjana.send_message(e.chat_id, 'Start Downloading')
	file_name = await anjana.download_media(amjana, pamka)
	path = pamka+noize
	await snd.edit('Success !!\n Path: '+path)
    
	#await snd.edit('Now uploading to AnonFile')
	url = 'https://tmp.ninja/upload.php'
	payload = open(f"{path}")
	r = requests.post(url, data=payload)
	print(r)
	print(type(r))