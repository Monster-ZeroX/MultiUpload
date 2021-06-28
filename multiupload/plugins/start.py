from multiupload import anjana
from telethon.sync import events
from telethon.tl.functions.users import GetFullUserRequest

@anjana.on(events.NewMessage(pattern='/start'))
async def start(e):
  xx = await e.get_chat()
  welcome = f'''Hey [{xx.first_name}](tg://user?id={xx.id}) 💛
How are you ??'''
  await anjana.send_message(e.chat_id, welcome)

@anjana.on(events.NewMessage(pattern='/help'))
async def help(e):
  helpmsg = f'''Here the help menu 😌
Reply to any file as **/anonfile**.'''
  await anjana.send_message(e.chat_id, helpmsg)