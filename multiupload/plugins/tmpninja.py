import shlex
import json
import subprocess

import asyncio, json, os
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
  cURL = f"""curl -i -F files[]=@{path} https://tmp.ninja/upload.php"""

  lCmd = shlex.split(cURL) # Splits cURL into an array

  p = subprocess.Popen(lCmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  out, err = p.communicate() # Get the output and the err message

  json_data = json.loads(out.decode("utf-8"))

  print(json_data) # Display now the data
