# Exercise 1 — Task Queue Simulator
# Concept: sequential execution + blocking
#
# Scenario
# You’re building a simple task runner that processes jobs one at a time.
#
# Requirements
# 1. Create a function run_task(task_name, duration)
# 2. Print when the task starts
# 3. Pause for duration seconds
# 4. Print when the task finishes
# 5. Process tasks in order

import time

def run_task(task_name, duration):
    print(f"Starting {task_name}")
    time.sleep(duration)
    print(f"Finished {task_name}")

#Given
tasks = [
    ("download_data", 2),
    ("process_data", 3),
    ("save_results", 1)
]

for task in tasks:
    run_task(task[0], task[1])

# Expected behavior (order matters)
# Starting download_data
# Finished download_data
# Starting process_data
# Finished process_data
# Starting save_results
# Finished save_results