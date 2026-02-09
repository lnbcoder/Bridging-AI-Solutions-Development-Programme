# Handle the case where the user enters something that isn’t a number.
# Task
# 1. Ask the user to enter their age.
# 2. Convert the input to an integer.
# 3. Print their age.
# 4. If they enter something invalid (like "ten"), catch the error and print a helpful message.
#
# Hint
# This error happens during type conversion, not input.

try:
    age = int(input("Enter age: "))
    print("You are {} years old.".format(age))
except:
    print("Invalid input. You must enter numbers(10) and not 'ten'.")