# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

# Example:
# string_repeater("q", 4)  #-> 'qqqq'
# string_repeater("go", 2) #-> 'gogo'
# string_repeater("tac", 3) #-> 'tactactac'

def string_repeater(text, n):
    str = ""
    for i in range(n):
        str += text
    return str

print(string_repeater("q", 4))
print(string_repeater("go", 2))
print(string_repeater("tac", 3))