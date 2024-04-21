import interactions
from interactions import Intents

bot = interactions.Client(intents=Intents.ALL, token="MTIyNzY3NjA0ODgxMzA2ODM3OQ.GVtb_R.JrTDAa-wVeibuQo9pTyX_YgzHcTMjuM08DXTyU" )

bot.load_extension("apps.nie.jurigged")
bot.load_extension("apps.quote.jurigged")
bot.load_extension("commands.purge.jurigged")
bot.load_extension("commands.ask.jurigged")
bot.load_extension("apps.chat.jurigged")

bot.start('MTIyNzY3NjA0ODgxMzA2ODM3OQ.GVtb_R.JrTDAa-wVeibuQo9pTyX_YgzHcTMjuM08DXTyU')


