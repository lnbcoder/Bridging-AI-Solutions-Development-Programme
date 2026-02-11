# Task
# (No real files yet — just simulating behavior)
# 1. Print "Opening file..." inside try.
# 2.Ask the user for a number.
# 3. Convert it to an integer.
# 4. If conversion fails, catch the error.
# 5. Use finally to print "Closing file..."
# Even if input fails, the “file” must close.

try:
    print("Opening file...")
    number = int(input("Enter number: "))
    print("The number you entered is", number)
except:
    print("Something went wrong...")
finally:
    print("Closing file...")
