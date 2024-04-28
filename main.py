import interactions
from interactions import Intents

bot = interactions.Client(intents=Intents.ALL, token="" )

bot.load_extension("apps.nie")
bot.load_extension("apps.quote")
bot.load_extension("commands.purge")
bot.load_extension("commands.ask")
bot.load_extension("apps.chat")

bot.start('')


