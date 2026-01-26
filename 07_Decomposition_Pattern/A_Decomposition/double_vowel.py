# Write a function `double_vowel` that accepts a string as an argument.
# The function should return a new string where **every vowel** in the original string is repeated **twice consecutively**.
# Vowels are: `a, e, i, o, u`

def double_vowel(str):
    vowels = list('aeiou')
    new_str = ""
    for i in str:
        if i in vowels:
            new_str += i * 2
        else:
            new_str += i
    return new_str

if __name__ == "__main__":
    print(double_vowel("runner"))
    # 'ruunneer'

    print(double_vowel("stoplight"))
    # 'stoopliight'

    print(double_vowel("gardener"))
    # 'gaardeeneer'
