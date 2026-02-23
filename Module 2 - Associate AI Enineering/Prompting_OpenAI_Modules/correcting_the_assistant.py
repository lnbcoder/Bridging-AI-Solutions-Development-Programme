# Create a message history where:
# User asks: "Is 5 a prime number?"
# Assistant incorrectly says: "No, it is not."
# User responds: "Are you sure? Please think again carefully."
# Send this conversation and print the response.
# Goal: See how the model reacts to correction pressure.

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
    messages = [{
        "role":"user", "content":"Is 5 a prime number?",
        "role":"assistant", "content":"No, it is not.",
        "role":"user", "content":"Are you sure? Please think again carefully."
    }]
)

print(response.choices[0].message.content)
