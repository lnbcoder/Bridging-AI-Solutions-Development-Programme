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
        ]
    )
    return response.choices[0].message.content


# Craft a prompt that asks the model for the function
prompt = f"""write a Python function that receives a list of 12 floats representing monthly sales data as input and, returns the month with the highest sales value as output."""

response = get_response(prompt)
print(response)
