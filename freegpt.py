import g4f
import time
import logging
from g4f.Provider import (
    AItianhu,
    Aichat,
    Bard,
    Bing,
    ChatBase,
    ChatgptAi,
    OpenaiChat,
    Vercel,
    You,
    Yqcloud,
)



def ask_gpt(messages:list):
       
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        provider=ChatgptAi(),
        n = 1,
        max_tokens = 1000,
        temperature = 0.5
    )
    print(response)
    return response

messages = []
while True:
    question = input("Question: ")
    messages.append({"role": "user", "content": question})
    answer = ask_gpt(messages=messages)
    messages.append({"role": "assistant", "content": answer})


