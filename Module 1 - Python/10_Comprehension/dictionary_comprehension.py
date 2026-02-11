# Given:
# sentence = "comprehensions are super useful"
# Create a dictionary where:
# - keys → each unique character (ignore spaces)
# - values → how many times that character appears

sentence = "comprehensions are super useful"
char_count = {char: sentence.count(char) for char in sentence.replace(" ","")}
print(char_count)

