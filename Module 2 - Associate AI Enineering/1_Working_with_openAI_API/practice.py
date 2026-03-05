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
    max_completion_tokens = 100,
    messages = [
        {"role":"user","content":"Identify any software principle?"}
    ]
)

print(response.choices[0].message.content)
