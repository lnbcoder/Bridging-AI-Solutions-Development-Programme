#Write a function `divisible(num1, num2)` 
# that returns **True** if `num1` is divisible by `num2`, 
# otherwise **False**.

# Example Output:
# print(divisible(12, 3))    # True
# print(divisible(12, 5))    # False
# print(divisible(60, 4))    # True
# print(divisible(60, 11))   # False
# print(divisible(21, 7))    # True
#print(divisible(21, 6))    # False

def divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
    
print(divisible(12, 3))    # True
print(divisible(12, 5))    # False
print(divisible(60, 4))    # True
print(divisible(60, 11))   # False
print(divisible(21, 7))    # True
print(divisible(21, 6))    # False

