# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.
 
def remove_first_vowel(s):
    s_list = list(s)
    vowels = "aeiou"

    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list.remove(s_list[i])
            break
        
    return "".join(s_list)


print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'
