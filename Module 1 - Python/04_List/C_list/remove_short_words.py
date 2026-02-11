# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

# Example:
# remove_short_words("knock on the door will you") -> 'knock door will'
# remove_short_words("a terrible plan") -> 'terrible plan'
# remove_short_words("run faster that way") -> 'faster that'

def remove_short_words(sentence):
    words = sentence.split()
    for i in words:
        if len(i) < 4:
            words.remove(i)
    new_sentence = " ".join(words)
    return new_sentence

print(remove_short_words("knock on the door will you")) # -> 'knock door will'
print(remove_short_words("a terrible plan")) # -> 'terrible plan'
print(remove_short_words("run faster that way")) # -> 'faster that'  