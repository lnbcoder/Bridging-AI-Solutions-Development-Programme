#%%
from transformers import pipeline

classifier=pipeline(
task="text-classification",
model="distilbert-base-uncased-finetuned-sst-2-english"
)

result=classifier("I hate waiting in long queues")
print(result)
# %%
