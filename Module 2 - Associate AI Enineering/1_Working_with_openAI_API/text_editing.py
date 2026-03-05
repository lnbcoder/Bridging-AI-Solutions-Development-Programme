import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env fill")

client = OpenAI(api_key=api_key)

prompt = """Update the following biography:
- Change the name to Sarah
- Change pronouns to she/her
- Change job title to Senior Software Engineer
biography: Alex is a software developer. He works at a startup and loves teaching programming.
"""
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role":"user", "content":prompt}],
    max_completion_tokens = 100,

)

print(response.choices[0].message.content)