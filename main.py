import interactions
from interactions import Intents
import os
from dotenv import load_dotenv
load_dotenv()
bot = interactions.Client(intents=Intents.ALL)

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

bot.load_extension("commands.purge")
bot.load_extension("commands.ask")
bot.load_extension("apps.chat")

bot.start(os.getenv('TOKEN'))


