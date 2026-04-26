from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[
        {"role":"system","content":"You are a helpful assistant"},
        {"role":"user","content":"Explain what an API is"}
    ]
)

print(response.choices[0].message.content)
