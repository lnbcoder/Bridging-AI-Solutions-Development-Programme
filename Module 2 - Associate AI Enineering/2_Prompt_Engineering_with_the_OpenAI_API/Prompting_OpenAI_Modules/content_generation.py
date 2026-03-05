import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

prompt = """Give the eye catching slogan for a restaurant with Italian, Chinese food and fine-dining, fast-food etc """

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{
        "role":"user","content":prompt
    }],
    max_completion_tokens = 100
)

print(response.choices[0].message.content)