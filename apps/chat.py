from interactions import listen, Extension

from hugchat import hugchat
from hugchat.login import Login
EMAIL = "arek.jkirejczyk@gmail.com"
PASSWD = "Fufkicztery4"
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.switch_llm(1)

async def fetch_message_history(channel, limit=5):
    messages_text = ""
    messages = await channel.history(limit=limit).flatten()
    for message in reversed(messages):
        messages_text += f"{message.author.display_name}: {message.content}\n"
    return messages_text


import asyncio

# Define a lock
response_lock = asyncio.Lock()

class Chat(Extension):
    @listen()
    async def on_message_create(self, event):
        if event.message.author == self.bot.user:
            return
        if event.message.channel.name == "chatting":
            async def generate():
                msg = await event.message.channel.send("*Generating...*")
                async with response_lock:
                    messages1 = await fetch_message_history(event.message.channel)
                    print(messages1)
                    retries = 5
                    for _ in range(retries):
                        try:
                            chatbot.new_conversation(switch_to = True)
                            response_tokens = []
                            for resp in chatbot.query("Please, keep your responses very short\n" + messages1 + "Klyda:", stream=True):
                                if resp is not None and "token" in resp:
                                    response_tokens.append(resp["token"])
                                    response = ("".join(response_tokens))
                                    await msg.edit(content=(response))
                                    
                            if not response_tokens:
                                print("Response tokens empty, retrying...")
                                continue

                            break
                        except Exception as e:
                            print(f"An exception occurred: {e}, retrying...")
            # Run the generation process while respecting the lock
            await generate()

