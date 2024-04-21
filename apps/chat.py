from interactions import listen, Extension, Task

from hugchat import hugchat
from hugchat.login import Login
EMAIL = "arek.jkirejczyk@gmail.com"
PASSWD = "Fufkicztery4"
cookie_path_dir = "./cookies/"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
chatbot.switch_llm(0)

async def fetch_message_history(channel, limit=10):
    messages_text = ""
    messages = await channel.history(limit=limit).flatten()
    for message in reversed(messages):
        messages_text += f"{message.author.display_name}: {message.content}\n"
    return messages_text

class Chat(Extension):
    @listen()
    async def on_message_create(self, event):
        if event.message.author == self.bot.user:
            return
        if event.message.channel.name == "chatting":
            generate.start()
        return event
        
@Task.create()
async def generate(event):
    messages1 = await fetch_message_history(event.message.channel)
    msg = await event.message.channel.send("*Generating...*")
    retries = 5
    for _ in range(retries):
        try:
            response_tokens = []
            for resp in chatbot.query(messages1 + "Klyda:", stream=True):
                if resp is not None and "token" in resp:
                    response_tokens.append(resp["token"])
                    response = ("".join(response_tokens))
                    print("Response:", response)
                    await msg.edit(content=(response))
            if not response_tokens:
                print("Response tokens empty, retrying...")
                continue

            break
        except Exception as e:
            print(f"An exception occurred: {e}, retrying...")

