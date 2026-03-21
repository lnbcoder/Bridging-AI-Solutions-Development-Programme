#%%
from transformers import pipeline

summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)

text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights from data.
It combines statistics, computer science, and domain expertise.
"""

result = summarizer(text)
print(result)

# %%
