from bot import anjana

@anjana(pattern="/start")
async def _(event):
	welcomemsg = '''Hey There. Welcome to Multi Uploader
	
	Channel: @Harp_Tech
	Group: @Harp_Chat'''
	await anjana.send_message(event.chat_id, welcomemsg)