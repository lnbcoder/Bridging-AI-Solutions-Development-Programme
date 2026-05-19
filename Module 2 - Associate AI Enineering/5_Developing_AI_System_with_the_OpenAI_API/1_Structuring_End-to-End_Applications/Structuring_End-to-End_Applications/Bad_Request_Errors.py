#%%
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

try:
  response=client.chat.completions.create(
  model="gpt-4.1-mini",
  messages=[
          {"role":"teacher","content":"Explain what an API is"}  # Using Teacher instead of User
      ]
  )

  print(response.choices[0].message.content)
  
except Exception as e:
  print("Something went wrong. Could be a Bad Request Errors.")


# %%
