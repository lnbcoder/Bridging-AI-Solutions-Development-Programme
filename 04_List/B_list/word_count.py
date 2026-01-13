# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

# Example:
# word_count("open the window please", ["please", "open", "sorry"]) -> 2
# word_count("drive to the cinema", ["the", "driver"]) -> 1
# word_count("can I have that can", ["can", "I"]) -> 3

def word_count(sentence, target_words):
    list_words = sentence.split(" ")
    word_count = 0

    for word in list_words:
        if word in target_words:
            word_count += 1

    return word_count

    
print(word_count("open the window please", ["please", "open", "sorry"])) # -> 2
print(word_count("drive to the cinema", ["the", "driver"])) # -> 1
print(word_count("can I have that can", ["can", "I"])) # -> 3