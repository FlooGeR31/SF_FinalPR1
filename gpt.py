import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.5,
        TimeoutError = 20
    )
    if completions.choices[0].text == "" and completions.choices[0].text == None:
        raise TimeoutError
    elif completions and completions.choices:
        message = completions.choices[0].text.strip()
        return message

res = generate_response("Привет, как у тебя дела? Какая погода в Белгороде?")
print(res)