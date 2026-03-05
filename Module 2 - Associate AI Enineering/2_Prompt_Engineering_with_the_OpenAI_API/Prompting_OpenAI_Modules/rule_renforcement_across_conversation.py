# Part 3: System + User + Assistant Roles
# Create:
'''
    system: "You must answer in one sentence only."

    user: "What is machine learning?"

    assistant: (leave this out — let the model respond first and save it)

    Then send another request including the assistant’s reply plus:
    "Explain it again in simpler terms."
'''

# Goal: Observe whether the one-sentence rule continues to apply.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

messages = [
    {"role":"system","content":"You must answer in one sentence only."},
    {"role":"user","content":"What is machine learning?"},
    {"role":"assistant","content":"(leave this out — let the model respond first and save it)"},
    {"role":"user","content":"Explain it again in simpler terms."}
]

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    max_completion_tokens = 150,
    messages = messages
)

print(response.choices[0].message.content)
