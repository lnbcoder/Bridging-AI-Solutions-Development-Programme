#%%
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

response=client.chat.completions.create(
model="gpt-4.1-mini",
response_format={"type":"json_object"},
messages=[
        {
"role":"user",
"content":"List five trees with their scientific names in JSON format"
        }
    ]
)

