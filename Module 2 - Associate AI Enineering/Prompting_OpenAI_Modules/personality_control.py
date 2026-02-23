# Personality Control
# Create a script that:
#  1.Uses a system message to make the assistant act like a strict math teacher.
#  2.Uses a user message that asks:
#   "Explain what 12 * 8 equals."
#  3.Prints the result.
# Goal: Observe how much the system message controls tone and style.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in the .env")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role":"system","content":"act like a strict math teacher"},
        {"role":"user","content":"Explain what 12 * 8 equals."}
    ],
    max_completion_tokens = 100
)

print(response.choices[0].message.content)
