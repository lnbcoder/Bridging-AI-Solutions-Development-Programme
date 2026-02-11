# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    word_list = sentence.split(" ")
    vowels = "aeiou"
    for i in range(len(word_list)):
        word = word_list[i]
        if len(word) > 4:
            new_word = ""
            for j in range(len(word)):
                if word[j] not in vowels:
                    new_word += word[j]
            word_list[i] = new_word
    
    return " ".join(word_list)


print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
