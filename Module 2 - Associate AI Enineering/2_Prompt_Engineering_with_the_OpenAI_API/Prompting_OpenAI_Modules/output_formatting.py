# Create a script where:

#  The system role says:
#  "You must respond only in valid JSON with keys: title and summary."

#  The user role asks:
#  "Explain what a Python dictionary is."

# Goal: See how system instructions can enforce structure.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key = api_key)


response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"system","content":"You must respond only in valid JSON with keys: title and summary."},
        {"role":"user","content":"Explain what a Python dictionary is."}
    ]
)

print(response.choices[0].message.content)

