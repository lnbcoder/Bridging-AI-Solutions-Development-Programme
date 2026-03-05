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

# Create the instructions
instructions = instructions = (
    "Determine the language of the following text and generate a suitable title for it. "
    "Use the provided output format. The text will be delimited using triple backticks."
)

# Create the output format
output_format = (
    "Text:\n"
    "Language:\n"
    "Title:"
)

# Define the text to analyze
text = """La inteligencia artificial está transformando el mundo moderno."""


# Create the final prompt
prompt = f"""
{instructions}

Output format:
{output_format}

Text to analyze:
'''{text}'''
"""
response = get_response(prompt)
print(response)
