from interactions import message_context_menu, Message, Extension, ContextMenuContext
class Nie(Extension):
    @message_context_menu(name="nie")
    async def repeat(self, ctx: ContextMenuContext):
        message: Message = ctx.target
        await ctx.send("NIE")