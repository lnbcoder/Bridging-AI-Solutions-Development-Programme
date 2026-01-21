# Write a function `word_replace` that accepts:
# - a sentence string
# - a dictionary
# The function should return a new sentence where words that appear as keys in the dictionary are replaced with their corresponding values.

def word_replace(sentence, dict):
    words = sentence.split(" ")
    for i in range(len(words)):
        if words[i] in dict:
            words[i] = dict[words[i]]
    return " ".join(words)

print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'

