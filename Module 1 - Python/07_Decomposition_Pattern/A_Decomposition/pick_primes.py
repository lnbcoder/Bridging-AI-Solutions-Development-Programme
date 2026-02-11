# Write a function `pick_primes` that accepts a list of numbers.
# The function should return a **new list** containing **only the prime numbers** from the original list.
# You may want to **reuse the `is_prime` function**.

from is_prime import is_prime

def pick_primes(list_of_numbers):
    new_list = []
    return new_list

print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []

