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
        max_completion_tokens=200
    )
    return response.choices[0].message.content

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""
modify the function according to the specified requirements: test if the inputs to the functions are positive, and if not, display appropriate error messages, otherwise return the area and perimeter of the rectangle.

```{function}```
"""

response = get_response(prompt)
print("Fisrt response: ", response)


# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f""" Explain your chan-of-thought, describe the function step by step ```{function}``` """
 
response = get_response(prompt)
print("Second response: ", response)
