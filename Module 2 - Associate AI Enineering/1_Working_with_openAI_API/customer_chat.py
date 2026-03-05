import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

cliet = OpenAI(api_key=api_key)

chat = """
Customer: My internet is very slow.
Agent: I’m sorry to hear that. Have you tried restarting the router?
Customer: Yes, but it didn’t help.
Agent: I will escalate this issue to our technical team.
"""
prompt =f"Summarize the following customer support chat in 2 sentences:\n{chat}"

response = cliet.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role":"user", "content":prompt}],
    max_completion_tokens = 100
)

print(response.choices[0].message.content)