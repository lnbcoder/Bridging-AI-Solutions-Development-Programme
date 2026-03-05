# Manually create a message history:
"""
[
  {"role": "user", "content": "What is a variable in Python?"},
  {"role": "assistant", "content": "A variable stores data."},
  {"role": "user", "content": "Can you give me an example?"}
]
"""
# Send this to the model and print the output.

# Goal: Understand that the model reads previous assistant replies as context.

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
        {"role": "user", "content": "What is a variable in Python?"},
        {"role": "assistant", "content": "A variable stores data."},
        {"role": "user", "content": "Can you give me an example?"}
    ],
    max_completion_tokens = 100

)

print(response.choices[0].message.content)
