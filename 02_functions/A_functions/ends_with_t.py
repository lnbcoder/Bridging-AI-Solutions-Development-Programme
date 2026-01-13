# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".

# print(ends_with_t("smart"))      # True
# print(ends_with_t("racket"))     # True
# print(ends_with_t("taco"))       # False
# print(ends_with_t("boomerang"))  # False

def ends_with_t(str):
    if str.endswith('t'):
        return True
    else:
        return False

print(ends_with_t("smart"))
print(ends_with_t("racket"))
print(ends_with_t("taco"))
print(ends_with_t("boomerang"))