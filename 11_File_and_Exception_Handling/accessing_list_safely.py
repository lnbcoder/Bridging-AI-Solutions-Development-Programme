# Task
# 1. Create a list with 5 items.
# 2. Ask the user for an index number.
# 3. Print the item at that index.
# 4. If the index is out of range, handle the error gracefully.
#
# Hint
# This is a very common runtime error in real projects.
from operator import index

try:
    names = ['Loveness', 'Ntshuxeko', 'Baloyi']
    user_index = input("Enter index number(0-2): ")
    print(names[user_index])
except:
    print("index is out of range")