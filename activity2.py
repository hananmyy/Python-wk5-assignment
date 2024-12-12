# Base Class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived Class: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Derived Class: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Derived Class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

# Derived Class: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Demonstrating Polymorphism
def show_move(vehicle):
    print(vehicle.move())

# Creating instances of each class
car = Car()
plane = Plane()
bicycle = Bicycle()
boat = Boat()

# Using polymorphism to call the same method move() on different objects
show_move(car)
show_move(plane)
show_move(bicycle)
show_move(boat)
