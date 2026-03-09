#%%
from dotenv import load_dotenv
import os
from huggingface_hub import InferenceClient

load_dotenv()

api_key=os.environ["HF_TOKEN"]

if not api_key:
    raise ValueError("HF_TOKENnot found in .env file")

client = InferenceClient(
    provider="together",
    api_key=api_key,
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(completion.choices[0].message.content)


# %%
