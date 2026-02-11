# Task
# 1.Ask the user for a number.
# 2. Divide 10 by that number.
# 3. Catch a division by zero error.
# 4. Use finally to print "Goodbye!"
# "Goodbye!" must print whether an error happens or not.

try:
    number = int(input("Enter number: "))
    answer = 10 / number
    print("10 divided by {} is {}".format(number,answer))
except:
    print("Something went wrong. You can't divide by zero.")
finally:
    print("Goodbye!")