# Create a class Counter with:
# - an instance variable count starting at 0
# - a method increment() that increases it by 1
# Call increment() three times and print the result.

class Counter:
    def __init__(self,count = 0):
        self.count = count

    def increment(self):
        self.count += 1

count = Counter()
count.increment()
count.increment()
count.increment()

print(count.count)