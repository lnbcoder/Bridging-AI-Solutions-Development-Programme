# Exercise 1: Sentiment Classification
# You want the model to label the sentiment of a product review as:
# -> Positive
# -> Negative
# -> Neutral

# Task:
# Write a zero-shot prompt that asks the model to classify this review:

# “The phone works fine, but the battery life is disappointing.”


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    max_completion_tokens = 150,
    messages = [
        {"role":"user","content":"The sentiment of a product review as: Positive, Negative, Neutral. Classify this review: 'The phone works fine, but the battery life is disappointing.'"}
    ]
)

print(response.choices[0].message.content)
