from interactions import Extension, slash_command, SlashContext
class Purge(Extension):
    @slash_command(name="purge", description="Just purge.")
    async def purging(self, ctx: SlashContext):
        ctx.defer
        await ctx.send("RoObienie czystki :DDD")
        await ctx.channel.purge(search_limit=1000, deletion_limit=1000)