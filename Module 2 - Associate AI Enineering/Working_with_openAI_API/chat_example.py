# uv add openai 

from openai import OpenAI # Create a client (make sure your OPENAI_API_KEY is set in your environment)
client = OpenAI()# Replace the prompt below with your own question or instruction

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=100,

    # Enter your prompt
    messages=[{"role": "user", "content": "Update the following biography: Change the name to Sarah, Change pronouns to she/her, Change job title to Senior Software Engineer. Alex is a software developer. He works at a startup and loves teaching programming."}]
)

print(response.choices[0].message.content)
