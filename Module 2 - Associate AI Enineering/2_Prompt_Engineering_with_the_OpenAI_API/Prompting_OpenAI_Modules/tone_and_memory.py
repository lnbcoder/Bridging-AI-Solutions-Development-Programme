# Part 3: System + User + Assistant Roles
# Create a conversation where:
'''
system: "You are a pirate speaking in pirate slang."
user: "What is Python programming?"
assistant: (you write a short pirate-style reply manually)
user: "Can you give me a simple code example?"
'''
# Send this full history and print the result.

# Goal: See how the system tone + prior assistant response influence the next reply.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    max_completion_tokens = 150,
    messages = [
        {"role":"system", "content":"You are a pirate speaking in pirate slang."},
        {"role":"user", "content":"What is Python programming?"},
        {"role":"assistant", "content":"You write a short pirate-style reply manually"},
        {"role":"user", "content":"Can you give me a simple code example?"}
    ]
)

print(response.choices[0].message.content)
