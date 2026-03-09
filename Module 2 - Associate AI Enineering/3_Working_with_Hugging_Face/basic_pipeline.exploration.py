# Question 1 — Basic Pipeline Exploration
# Build a text generation pipeline using GPT-2 that:

# Uses the prompt "The future of technology"
# Generates 3 different completions
# Limits each completion to 15 new tokens
# Prints each result numbered (e.g. Result 1: ..., Result 2: ...)


from transformers import pipeline

gpt2_pipeline = pipeline(task="text-generation",model="openai-community/gpt2")

results = gpt2_pipeline("The future of the technology", max_new_tokens = 15, num_return_sequences = 3)

count = 1
for result in results:
    print(f"Result {count}: {result['generated_text']}")
    count += 1



