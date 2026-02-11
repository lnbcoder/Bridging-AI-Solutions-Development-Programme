# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.
    
# Example:
# bleep_vowels("skateboard") #-> 'sk*t*b**rd'
# bleep_vowels("slipper") #-> 'sl*pp*r'
# bleep_vowels("range") #-> 'r*ng*'
# bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng


def bleep_vowels(str):
    new_str = ""
    vowel = "aeiou"

    for char in str:
        if char in vowel:
            new_str += "*"
        else:
            new_str += char

    return new_str


print(bleep_vowels("skateboard")) #-> 'sk*t*b**rd'
print(bleep_vowels("slipper")) #-> 'sl*pp*r'
print(bleep_vowels("range")) #-> 'r*ng*'
print(bleep_vowels("brisk morning")) #-> 'br*sk m*rn*ng'