# Create a class Car that:
# - has a class variable total_cars
# - increments it every time a new car is created
#
# Create 3 cars and print the total.

class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

car1 = Car("Mercedes Benz")
car2 = Car("BMW")
car3 = Car("Suzuki Fronx")

print(f"Total number of cars: {Car.total_cars}")
