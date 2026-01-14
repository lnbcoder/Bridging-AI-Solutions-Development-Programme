# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

# Example:
# alternating_caps("take them to school") -> 'take THEM to SCHOOL'
# alternating_caps("What did ThEy EAT before?") -> 'what DID they EAT before?'

def alternating_caps(sentence):
    words = sentence.split()
    new_sentence = ""
    word = ""

    for i in range(1, len(words) + 1):
        if i % 2 == 0:
            word = words[i - 1].upper()
        else:
            word = words[i - 1].lower()

        new_sentence += word + " "

    return new_sentence

print(alternating_caps("take them to school")) # -> 'take THEM to SCHOOL'
print(alternating_caps("What did ThEy EAT before?")) # -> 'what DID they EAT before?'