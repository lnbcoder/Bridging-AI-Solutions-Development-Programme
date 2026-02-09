# Use try / except to protect multiple risky operations.
# Task
# 1. Ask the user for a number.
# 2. Convert it to an integer.
# 3. Divide 100 by that number.
# 4. Handle both:
#   - invalid input
#   - division by zero
# For now, use one except block (we’ll split them later when you learn multiple exceptions).

try:
    number = int(input("Enter number: "))
    answer = 100 / number
    print(answer)
except:
    print("Something went wrong. Invalid input or can not divide by zero")
