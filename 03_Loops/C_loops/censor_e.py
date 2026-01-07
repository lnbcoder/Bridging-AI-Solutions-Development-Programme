# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

# Example:
# censor_e("speedy")  #-> 'sp**dy'
# censor_e("pending") #-> 'p*nding'
# censor_e("scene")   #-> 'sc*n*'
# censor_e("heat")    #-> 'h*at'

def censor_e(text):
    word = ''
    for i in text:
        if i == 'e':
            i = '*'
            word += i
        else:
            word += i
            
    return word

print(censor_e("speedy"))  #-> 'sp**dy'
print(censor_e("pending")) #-> 'p*nding'
print(censor_e("scene"))   #-> 'sc*n*'
print(censor_e("heat"))    #-> 'h*at'


