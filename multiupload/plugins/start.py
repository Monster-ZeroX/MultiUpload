from multiupload import anjana
from telethon.sync import events
from telethon.tl.functions.users import GetFullUserRequest

anjana.parse_mode = 'html'

@anjana.on(events.NewMessage(pattern='/start'))
async def start(e):
  xx = await e.get_chat()
  welcome = f'''Hey <a href="tg://user?id={xx.id}">{xx.first_name}</a> 💛
For More Help. Click <b>/help</b>'''
  await e.respond(e.chat_id, welcome)

@anjana.on(events.NewMessage(pattern='/help'))
async def help(e):
  helpmsg = f'''<b><u>Here the help menu 😌</u></b>

<b>/anonfile</b> - Upload files to AnonFile.
<b>/transfersh</b> - Upload files to TransferSH
<b>/gofile</b> - Upload files to GoFile

<i><b>Project of <a href="https://telegram.me/harp_tech">HARP Tech</a></b></i>'''
  await e.respond(e.chat_id, helpmsg)