# Create a class Person where:
# - name is required
# - age defaults to 0
# Create:
# - Person("Alice")
# - Person("Bob", 25)
# Print their ages.

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

person1 = Person("Alice")
person2 = Person("Loveness", 23)

print(f"Age for person1: {person1.age}")
print(f"Age for person2: {person2.age}")