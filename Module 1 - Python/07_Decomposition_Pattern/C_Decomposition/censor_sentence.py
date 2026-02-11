# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(sentence, target_words):
    new_sentence = []
    for word in sentence.split():
        if word in target_words:
            temp = '*' * len(word)
            new_sentence.append(temp)
        else:
            new_sentence.append(word)
    return ' '.join(new_sentence)


print(censor_sentence('where the heck is my celery', ['heck','celery']))
# 'where the **** is my ******'

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
# 'why you little **********'
