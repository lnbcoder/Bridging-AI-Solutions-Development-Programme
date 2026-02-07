# Given:
# numbers = list(range(1, 21))
# Create a list comprehension that returns the square of all numbers divisible by 3.

numbers = list(range(1, 21))
divisible_list = [number for number in numbers if number % 3 == 0]
print(divisible_list)