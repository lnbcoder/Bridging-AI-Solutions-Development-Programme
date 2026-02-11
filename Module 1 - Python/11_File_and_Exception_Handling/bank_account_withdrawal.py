# Custom Exceptions
# Scenario: Bank Account Withdrawal
# Exercise
# - Create a custom exception for insufficient funds.
#
# Task
# 1.Create a custom exception called InsufficientFundsError.
# 2.Create a variable balance = 500.
# 3.Ask the user how much they want to withdraw.
# 4.If withdrawal amount is greater than balance:
#  - raise InsufficientFundsError
# 5.Otherwise, subtract and print the new balance.

class InsufficientFundsError(Exception):
    pass

try:
    balance = 500
    withdraw = int(input("How much do want to withdraw: "))

    if withdraw > balance:
        raise InsufficientFundsError

    new_balance = balance - withdraw
    print("Withdrawal successful.")
    print(f"Your balance is now: R{new_balance}")

except InsufficientFundsError:
    print(f"Insufficient funds, your balance is R{balance}")