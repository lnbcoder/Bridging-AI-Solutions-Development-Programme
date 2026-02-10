# Exercise 4 — Checkout System
# Concept: control flow + blocking
#
# Scenario
# You’re building a checkout system that validates items sequentially.
#
# Requirements
# 1. Each item has a price
# 2. Reject items with price ≤ 0
# 3. Stop checkout if an invalid item is found
# 4. Print each step
import time

def validate_item(cart):
    total = 0
    for item in cart:

        print("Scanning item...")
        time.sleep(3)

        if item <= 0:
            print("Invalid item. Checkout stooped...\n")
            return
        else:
            print(f"Valid item: R{item}\n")
            total += item
    print("Checkout successful. Total: R", total)

# Given
cart = [25, 40, -10, 30]
validate_item(cart)