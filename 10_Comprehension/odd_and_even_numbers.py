# Given:
# numbers = range(1, 11)
# Create a list where:
# - Even numbers → "even"
# - Odd numbers → "odd"
# ⚠️ This requires an inline if–else, not a filter.

numbers = range(1, 11)
list_of_number = ["even" if number % 2 == 0 else "odd" for number in numbers]
print(list_of_number)