from transformers import pipeline

grammar_checker = pipeline(
    task="text-classification",
    model="abdulmatinomotoso/English_Grammar_Checker"
)

output = grammar_checker("I will walk dog")
print(output)