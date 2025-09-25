# Polymorphism Challenge! 🎭

class Animal:
    """A base class for all animals."""
    def __init__(self, name):
        self.name = name

    def speak(self):
        """A generic speak method. Subclasses must override this."""
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    """A class representing a dog."""
    def speak(self):
        """The dog's way of speaking."""
        print(f"{self.name} says: Woof! 🐶")

class Cat(Animal):
    """A class representing a cat."""
    def speak(self):
        """The cat's way of speaking."""
        print(f"{self.name} says: Meow! 🐱")

class Bird(Animal):
    """A class representing a bird."""
    def speak(self):
        """The bird's way of speaking."""
        print(f"{self.name} says: Chirp! 🐦")

# --- Main part of the script ---
if __name__ == "__main__":
    # Create a list of different animal objects
    animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Sky")]

    # Loop through the list and call the same method on different objects
    for animal in animals:
        animal.speak()  # Polymorphism in action!
