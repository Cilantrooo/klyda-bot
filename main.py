import interactions
from interactions import Intents
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = interactions.Client(intents=Intents.ALL)

bot.load_extension("commands.purge")
bot.load_extension("commands.ask")
bot.load_extension("apps.chat")

bot.start(TOKEN)


