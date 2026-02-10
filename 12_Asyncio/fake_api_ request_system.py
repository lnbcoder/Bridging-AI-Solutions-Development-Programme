# Exercise 3 — Fake API Request System
# Concept: blocking network calls (simulated)
#
# Scenario
# Simulate fetching user data from an API.
#
# Requirements
# 1. Create a function fetch_user(user_id)
# 2. Print when fetching starts
# 3. Sleep for 1–3 seconds (random)
# 4. Return a dictionary {id, name}
# 5. Fetch users one at a time
# 6. Store results in a list

import time
import random

def fetch_user(user_id):
    print("Fetching data...")
    time.sleep(random.randint(1,3))
    return {"user ID": user_id, "name": f"user{user_id}"}

# Given:
users = [101, 102, 103, 104]
results = []

for user_id in users:
    data = fetch_user(user_id)
    print(data, "\n")
    results.append(data)

print("Results:",  results)
