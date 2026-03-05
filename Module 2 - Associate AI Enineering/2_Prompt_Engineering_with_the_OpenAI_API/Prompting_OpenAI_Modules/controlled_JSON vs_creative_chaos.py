# See how temperature interacts with structured output.
'''
Create two calls with this system instruction:
  "You must respond only in valid JSON with keys: name and description."

User prompt:
  "Create a startup idea."

Call 1:
 temperature=0
 Use response_format={"type": "json_object"}

Call 2:
 temperature=1.3
 Same JSON rule enforced

Print both outputs.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def get_reponse(prompt, system, temperature):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_completion_tokens = 100,
        messages = [
            {"role":"system","content":system},
            {"role":"user","content":prompt}
        ],
        temperature = temperature
    )

    return response.choices[0].message.content

system = "You must respond only in valid JSON with keys: name and description."
prompt = "Create a startup idea."

print("First with temperature zero: ",get_reponse(prompt,system,0))
print("Second with temperature 1.2: ", get_reponse(prompt,system,1.2))
