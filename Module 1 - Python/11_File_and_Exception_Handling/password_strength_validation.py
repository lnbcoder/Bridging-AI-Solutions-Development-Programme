# Using raise
# Scenario: Password Strength Validation
# Exercise
# - You are validating a password.
#
# Task
# 1.Ask the user for a password.
# 2.If the password length is less than 8 characters:
#  - manually raise a ValueError
# 3.Otherwise, print "Password accepted".

password = input("Enter password: ")
try:
    if len(password) < 8:
        raise ValueError("Password length should not be less than 8 characters")
    else:
        print("Password accepted")
except ValueError as e:
    print("error: ",e)