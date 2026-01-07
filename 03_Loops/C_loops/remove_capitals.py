# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

# Example:
# remove_capitals("fOrEver")     #-> 'frver'
# remove_capitals("raiNCoat")    #-> 'raioat'
# remove_capitals("cElLAr Door") #-> 'clr oor'

def remove_capitals(text):
    text_output = ""
    for i in text:
        if i.islower() or i.isspace():
            text_output += i

    return text_output

print(remove_capitals("fOrEver"))    #-> 'frver'
print(remove_capitals("raiNCoat"))    #-> 'raioat'
print(remove_capitals("cElLAr Door")) #-> 'clr oor'
