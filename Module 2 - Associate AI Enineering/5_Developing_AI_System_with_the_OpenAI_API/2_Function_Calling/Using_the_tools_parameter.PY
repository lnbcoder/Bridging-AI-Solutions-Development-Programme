#%%
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

message_listing = """
   
    Beautiful 3-bedroom apartment for sale in New York.
    This modern apartment is listed at $750,000 and 
"""

function_definition = [
    {
        "type": "function",
        "function": {
            "name": "extract_property_info",
            "description": "Extract real estate property details",
            "parameters": {
                "type": "object",
                "properties": {
                    "house_type": {
                        "type": "string",
                        "description": "Type of the property (e.g., apartment, house)"
                    },
                    "location": {
                        "type": "string",
                        "description": "Location of the property"
                    },
                    "price": {
                        "type": "string",
                        "description": "Price of the property"
                    },
                    "bedrooms": {
                        "type": "integer",
                        "description": "Number of bedrooms"
                    }
                },
                "required": ["house_type", "location", "price", "bedrooms"]
            }
        }
    }
]

client = OpenAI(api_key=api_key)

def get_reponse(message, function): 
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an assistant that extracts structured data."},
        {"role": "user", "content": message}
    ],
    tools=function,
    tool_choice="auto"
)

# Extract tool call 
    return response.choices[0].message.tool_calls[0].function.arguments


print(get_reponse(message_listing, function_definition))