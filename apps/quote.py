from inspirational_quotes import quote
from interactions import message_context_menu, Message, Extension, ContextMenuContext
class Quote(Extension):
        @message_context_menu(name="quotes")
        async def send_quote(self, ctx: ContextMenuContext):
            dict = quote()
            str = ""
            for item in dict:
                str += item + dict[item]
            print(str)
            edited = str.replace("quote", "").replace("author", "\n - ").replace('"', "")
            message: Message = ctx.target
            await ctx.send(edited)

