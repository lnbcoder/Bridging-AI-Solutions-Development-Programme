# Understanding how temperature affects creativity.
'''
Write a script that:
1. ses the same prompt:
   "Write a short tagline for a futuristic coffee shop."

2. Calls the model twice:
 - First with temperature=0
 - Second with temperature=1.2

Prints both outputs clearly labeled.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def get_reponse(prompt, temperature):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_completion_tokens = 100,
        messages = [{"role":"user","content":prompt}],
        temperature = temperature
    )

    return response.choices[0].message.content

prompt = "Write a short tagline for a futuristic coffee shop."

print("First with temperature zero: ",get_reponse(prompt,0))
print("Second with temperature 1.2: ", get_reponse(prompt,1.2))
