# Write a function `keep_it_quiet` that accepts a string as an argument.
# The function should return the lowercase version of the string
# with 3 periods added to the end.

# print(keep_it_quiet("HOORAY"))     # "hooray..."
# print(keep_it_quiet("Doggo"))      # "doggo..."
# print(keep_it_quiet("WHAT?!?!"))   # "what?!?!..."

def keep_it_quiet(str):
    lower_case = str.lower()
    return lower_case

print(keep_it_quiet("HOORAY"))     # "hooray..."
print(keep_it_quiet("Doggo"))      # "doggo..."
print(keep_it_quiet("WHAT?!?!"))   # "what?!?!..."