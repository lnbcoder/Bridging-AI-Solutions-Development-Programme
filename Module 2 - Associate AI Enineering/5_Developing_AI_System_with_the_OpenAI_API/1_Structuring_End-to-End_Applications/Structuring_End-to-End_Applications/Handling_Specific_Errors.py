#%%
from dotenv import load_dotenv
import os
from openai import OpenAI
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

try:
    response=client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content":"List five data science profession"}],
   
    )
    print(response.choices[0].message.content)

except openai.AuthenticationError as e:
       print(f"Invalid API key. {e}")

# except openai.RateLimitError as e:
#         print(f"Too many requests. Please wait.{e}")
#except Exception as e:
    #print(f"Unexpected error occurred.{e}")


