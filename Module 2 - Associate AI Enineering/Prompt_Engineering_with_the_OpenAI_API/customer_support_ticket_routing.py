import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

def get_response(prompt):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role":"user","content":prompt}
        ],
        max_completion_tokens=250
    )

ticket = """Hello Support Team,

I was charged twice for my subscription this month, but I can only see one active plan in my account dashboard. 
I’ve already checked my payment history and bank statement, and the duplicate charge is still showing. 
Could you please look into this and help resolve the issue as soon as possible?

Thank you.
"""

# Craft a prompt to classify the ticket
prompt = f"""  classifies the ticket based on technical issue, billing inquiry, or product feedback, without providing anything else in the response.

```{ticket}```
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)
