#%%
from transformers import pipeline

classifier = pipeline("text-classification", model="mariagrandury/distilbert-base-uncased-finetuned-sms-spam-detection")

result = classifier("Congratulations! You've won a free iPhone. Click here now!")
print(result)


# %%
