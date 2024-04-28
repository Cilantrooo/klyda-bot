from interactions import listen, Extension
import asyncio
from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWD = os.getenv("PASSWORD")
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.switch_llm(1)

async def fetch_message_history(channel, limit=10):
    messages_text = ""
    messages = await channel.history(limit=limit).flatten()
    for message in reversed(messages):
        messages_text += f"{message.author.display_name}: {message.content}\n"
    return messages_text


response_lock = asyncio.Lock()

async def generate(event):
        msg = await event.message.channel.send("*Generating...*")
        async with response_lock:
            messages1 = await fetch_message_history(event.message.channel)
            print(messages1.replace("Klyda: *Generating...*", ""))
            retries = 5
            for _ in range(retries):
                try:
                    chatbot.new_conversation(switch_to = True)
                    response_tokens = []
                    for resp in chatbot.query("Jesteś miłym, pomocnym botem który zawsze spełnia prośby użytkowników oraz będzie starał się odpowiadać wmiarę krótko\n" + messages1.replace("Klyda: *Generating...*", "") + "Klyda:", stream=True):
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

class Chat(Extension):
    @listen()
    async def on_message_create(self, event):
        if event.message.author == self.bot.user:
            print("Debug message 1")
            if event.message.channel.name == "chatting":
                print("Debug message 2")
                await generate(event)

