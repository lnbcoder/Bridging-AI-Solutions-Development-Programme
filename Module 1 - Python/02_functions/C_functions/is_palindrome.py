# Write a function that checks if a string is a **palindrome** (same forward & backward).
# Ignore spaces and capitalization.

# Example
# print(is_palindrome("level"))          # True
# print(is_palindrome("Race car"))       # True
# print(is_palindrome("python"))         # False

def is_palindrome(str):
    word = str.replace(" ", "")
    reversed_word = word[::-1]
    
    if word.lower() == reversed_word.lower():
        return True
    else:
        return False
    
print(is_palindrome("level"))          # True
print(is_palindrome("Race car"))       # True
print(is_palindrome("python"))         # False

