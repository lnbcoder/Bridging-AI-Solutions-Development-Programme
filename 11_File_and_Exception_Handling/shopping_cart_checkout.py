# Catching Multiple Exceptions
# Scenario: Shopping Cart Checkout
# Exercise
# - A user is checking out an online cart.
#
# Task
# 1. Ask for item price.
# 2. Ask for quantity.
# 3. Calculate total price.
# 4. Handle:
#  - ValueError → invalid input
#  - ZeroDivisionError → quantity of zero used

try:
    item_price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    total_price = item_price * quantity
    print("Total price: R", total_price)

except ValueError:
    print("Invalid input. Price and quantity must be numbers.")

except ZeroDivisionError:
    print("Quantity can not be zero.")
