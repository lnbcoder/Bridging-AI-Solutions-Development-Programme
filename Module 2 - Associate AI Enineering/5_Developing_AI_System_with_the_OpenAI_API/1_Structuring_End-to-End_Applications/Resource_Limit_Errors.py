from dotenv import load_dotenv
import os
from openai import OpenAI
import time

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

for i in range(5):
 try:
response=client.chat.completions.create(
model="gpt-4.1-mini",
messages=[{"role":"user","content":"Tell me a joke"}]
        )
print(response.choices[0].message.content)

except Exception:
print("Rate limit reached. Waiting...")
time.sleep(5)
