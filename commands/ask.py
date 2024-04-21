from interactions import Extension, slash_command, slash_option, SlashContext, OptionType
import asyncio
from g4f.client import Client

class Ask(Extension):
    @slash_command(name="ask", description="Ask the stupid ai 🥰.")
    @slash_option(
        name="text_input",
        description="text input.",
        required=True,
        opt_type=OptionType.STRING,
        min_length=5,
        max_length=100
    )
    async def ask_generate(self, ctx: SlashContext, text_input: str):
        await ctx.defer()
        input_message = f"Hello, you are a helpful AI assistant discord bot. Text provided by the user: {text_input}"
        completion_result = await asyncio.to_thread(Client().chat.completions.create,
                                                    model="gpt-4",
                                                    messages=[{"role": "user", "content": input_message }]
                                                )
        response = completion_result.choices[0].message.content
        
        # Send response along with file content
        await ctx.send(response)