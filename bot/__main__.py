from sys import argv, exit
from bot import anjana
from bot import BOT_TOKEN

# IDK WHY IT'S SO IMPORTANT, JUST DON'T REMOVE THIS
import bot.events

try:
    anjana.start(bot_token=BOT_TOKEN)
except Exception as e:
    print(f"Error:\n\n {str(e)}")
    exit(1)

    anjana.run_until_disconnected()