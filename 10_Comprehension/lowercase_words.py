# Given:
# words = ["Python", "is", "POWERFUL", "and", "Fun"]
# Create a list of lowercase words that have more than 3 letters.

words = ["Python", "is", "POWERFUL", "and", "Fun"]
new_words = [word.lower() for word in words if len(word) > 3]
print(new_words)