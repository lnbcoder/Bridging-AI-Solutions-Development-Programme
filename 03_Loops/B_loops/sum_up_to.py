# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.
# Example:
# sum_up_to(4)  #-> 10
# sum_up_to(5)  #-> 15
# sum_up_to(2)  #-> 3

def sum_up_to(max_num):
    sum = 0
    for i in range(1, max_num + 1):
        sum += i

    return sum

num = int(input("Enter number: "))
print(sum_up_to(num))
