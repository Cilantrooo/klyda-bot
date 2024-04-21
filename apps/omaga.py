from interactions import message_context_menu, Message, Extension, ContextMenuContext
from discord_timestamps import format_timestamp
import datetime
import random

class DeathTime(Extension):
    @message_context_menu(name="omaga")
    async def repeat(self, ctx: ContextMenuContext):
        message: Message = ctx.target
        random.seed(42)
        await ctx.send(":)))", format_timestamp(datetime.datetime(random.randint(2024, 2080), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))))
