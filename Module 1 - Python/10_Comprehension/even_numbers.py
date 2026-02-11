# From a list:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a new list containing only even numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)