from multiupload import anjana
from telethon.sync import events
from telethon.tl.functions.users import GetFullUserRequest

@anjana.on(events.NewMessage(pattern='/start'))
async def start(e):
  xx = await e.get_chat()
  welcome = f'''Hey [{xx.first_name}](tg://user?id={xx.id}) 💛
For More Help. Click **/help**'''
  await anjana.send_message(e.chat_id, welcome)

@anjana.on(events.NewMessage(pattern='/help'))
async def help(e):
  helpmsg = f'''**--Here the help menu 😌--**

**/anonfile** - Upload files to AnonFile.
**/transfersh** - Upload files to TransferSH
**/gofile** - Upload files to GoFile
**/ufile** - Upload files to UFile

__**Project of [HARP Tech](https://telegram.me/harp_tech)**__'''
  await anjana.send_message(e.chat_id, helpmsg)