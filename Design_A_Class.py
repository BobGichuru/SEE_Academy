# Assignment: OOP with Inheritance and Polymorphism

# --- Part 1: Designing Classes with Inheritance ---

class Vehicle:
    """A base class representing a generic vehicle."""

    def __init__(self, brand, model, year):
        """Constructor to initialize a new Vehicle object."""
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        """Returns a user-friendly string representation of the vehicle."""
        return f"{self.year} {self.brand} {self.model}"

    def move(self):
        """A generic move method. Subclasses should override this."""
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    """A class representing a car, inheriting from Vehicle."""

    def move(self):
        """Overrides the parent move() method for a car."""
        print(f"The {self.brand} {self.model} is driving on the road. 🚗")


class Plane(Vehicle):
    """A class representing a plane, inheriting from Vehicle."""

    def __init__(self, brand, model, year, airline):
        """Constructor for Plane, adding an airline attribute."""
        # Call the parent class's constructor to set brand, model, and year
        super().__init__(brand, model, year)
        self.airline = airline  # Encapsulation: adding a specific attribute

    def move(self):
        """Overrides the parent move() method for a plane."""
        print(f"The {self.airline} {self.brand} {self.model} is flying in the sky. ✈️")


# --- Part 2: Polymorphism Challenge ---

if __name__ == "__main__":
    # Create instances of our classes
    my_car = Car("Toyota", "Camry", 2022)
    my_plane = Plane("Boeing", "747", 2015, "Emirates")

    # Create a list of different vehicle objects
    vehicles = [my_car, my_plane]

    # Loop through the list and call the same method on different objects
    for vehicle in vehicles:
        print(f"\nVehicle: {vehicle}")
        vehicle.move()  # Polymorphism in action!
