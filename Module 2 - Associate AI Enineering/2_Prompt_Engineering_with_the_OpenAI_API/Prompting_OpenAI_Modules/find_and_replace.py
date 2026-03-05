import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

client = OpenAI(api_key=api_key)

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal 
combustion engine or an electric motor. It has four wheels, and 
is designed to carry passengers and/or cargo on roads or highways. 
Cars have become a ubiquitous part of modern society, and are used for 
a wide variety of purposes, such as commuting, travel, and transportation 
of goods. Cars are often associated with freedom, independence, and mobility."""

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{
        "role":"user","content":prompt
    }],
    max_completion_tokens = 100
)

print(response.choices[0].message.content)