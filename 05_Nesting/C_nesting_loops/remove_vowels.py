# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(s):
    new_s = ""
    vowels = list("aeiou")
    for i in s:
        if i not in vowels:
            new_s += i
    return new_s        
    

print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'
