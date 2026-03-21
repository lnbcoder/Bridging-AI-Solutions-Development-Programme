#%%
from transformers import pipeline

summarizer = pipeline("summarization" , model="cnicu/t5-small-booksum")

original_text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
"""

summary_text =summarizer(original_text)

print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")
# %%
