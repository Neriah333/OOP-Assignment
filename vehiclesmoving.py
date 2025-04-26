class Vehicle:
    """
    Base class representing a vehicle.
    """
    def __init__(self, name, speed):
        """
        Constructor for the Vehicle class.
        """
        self.name = name
        self.speed = speed

    def move(self):
        """
        Abstract method to be overridden by subclasses.
        This method should define how the vehicle moves.
        """
        raise NotImplementedError("Subclass must implement the move() method")

    def __str__(self):
        return f"{self.name} moving at {self.speed} km/h"


class Car(Vehicle):
    """
    Represents a car, inheriting from Vehicle.
    """
    def __init__(self, name, speed, num_doors):
        """
        Constructor for the Car class.

        """
        super().__init__(name, speed)  # Call the parent class's constructor
        self.num_doors = num_doors

    def move(self):
        """
        Overrides the move() method to define how a car moves.
        """
        return f"{self.name} is driving on the road at {self.speed} km/h with {self.num_doors} doors. 🚗"

    def __str__(self):
        return f"{super().__str__()} and has {self.num_doors} doors"


class Plane(Vehicle):
    """
    Represents a plane, inheriting from Vehicle.
    """
    def __init__(self, name, speed, altitude):
        """
        Constructor for the Plane class.

        
        """
        super().__init__(name, speed)  # Call the parent class's constructor
        self.altitude = altitude

    def move(self):
        """
        Overrides the move() method to define how a plane moves.
        """
        return f"{self.name} is flying in the sky at {self.speed} km/h and an altitude of {self.altitude} meters. ✈️"

    def __str__(self):
        return f"{super().__str__()} and flying at {self.altitude} meters"


# Create instances of the classes
my_car = Car("Toyota Camry", 120, 4)
my_plane = Plane("Boeing 747", 900, 10000)

# Demonstrate polymorphism - calling the move() method on different objects
print(my_car.move())  # Output: Toyota Camry is driving on the road at 120 km/h with 4 doors. 🚗
print(my_plane.move())  # Output: Boeing 747 is flying in the sky at 900 km/h and an altitude of 10000 meters. ✈️

print(my_car)
print(my_plane)
