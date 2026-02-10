# Exercise 5 — Timing & Observation (IMPORTANT)
# Concept: understanding blocking deeply
#
# Scenario
# Measure how long synchronous execution takes.
#
# Requirements
# 1. Use time.time() or time.perf_counter()
# 2. Call a function 3 times
# 3. Each call sleeps for 2 seconds
# 4. Print total runtime
# 5. Explain why it took that long (in comments)

import time

start_time = time.time()
print("Task 1 running...")
time.sleep(2)
print("Task 2 running...")
time.sleep(2)
print("Task 3 running...")
time.sleep(2)
end_time = time.time()

print(f"Total runtime: {end_time - start_time}")

# In my understanding, the code took long to run because in synchronous, the code needs
# to run and finish the first task before moving to the next
