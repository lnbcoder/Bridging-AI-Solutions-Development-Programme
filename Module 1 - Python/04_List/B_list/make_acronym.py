# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

# Example:
# make_acronym("New York") -> 'NY'
# make_acronym("same stuff different day") -> 'SSDD'
# make_acronym("Laugh out loud") -> 'LOL'
# make_acronym("don't over think stuff") -> 'DOTS'

def make_acronym(sentence):
    string = ""
    for i in sentence.split(" "):
        string += i[0].capitalize()

    return string

print(make_acronym("New York")) # -> 'NY'
print(make_acronym("same stuff different day")) # -> 'SSDD'
print(make_acronym("Laugh out loud")) # -> 'LOL'
print(make_acronym("don't over think stuff")) # -> 'DOTS'