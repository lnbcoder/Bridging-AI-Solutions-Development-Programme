# Using try / except / finally including raise
# Scenario: Network Connection Cleanup
# Exercise
# - You are simulating a network request.
# Task
# 1. Print "Connecting to server...".
# 2. Ask the user how long the request should take (seconds).
# 3. Convert the input to an integer.
# 4. If the number is negative, a ValueError should occur naturally.
# 5. Use finally to print "Connection closed." no matter what.

try:
    print("Connecting to server...")
    request_time = int(input("How long should the request take (seconds): "))
    print("Request time {}".format(request_time))

    if request_time < 0:
        raise ValueError

except ValueError:
    print("Error: seconds can't be negative...")
finally:
    print("Connection closed...")