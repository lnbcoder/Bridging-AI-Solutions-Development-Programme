# Create a class Car that:
# - has a class variable total_cars
# - increments it every time a new car is created
#
# Create 3 cars and print the total.

class Car:
    total_cars = 0

    def increment(self):
        Car.total_cars += 1

car1 = Car()
car1.increment()

car2 = Car()
car2.increment()

car3 = Car()
car3.increment()

print(f"Total number of cars: {Car.total_cars}")
