import openai
from config import Chatbot

# ChatGPT Setting
openai.api_key = Chatbot.OPENAI_KEY
MODEL = Chatbot.MODEL

def chat(msg: str, history: list = []):
    messages = []
    SYSTEM_MSG = Chatbot.SYSTEM_PROMPT

    messages.append({"role":"system", "content":SYSTEM_MSG})
    history.append({"role":"user", "content":msg})
    messages.extend(history)

    chatbot = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )

    bot_msg = chatbot["choices"][0]["message"]["content"]
    history.append({"role":"assistant", "content":bot_msg})
    
    return bot_msg, history

if __name__ == "__main__":
    first = True
    history = []
    while True:
        if first:
            print("Bot >> ", end="")
            msg = chat(1, "안녕")
            print(msg)
            first = False
        print("Message >> ", end="")
        str = input();
        print("Bot >> ", end="")
        msg = chat(1, str)
        print(msg)