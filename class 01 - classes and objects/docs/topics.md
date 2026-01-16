# Class 1: Classes and Objects

## Overview
In this class, we introduce Object-Oriented Programming (OOP) fundamentals in Python. We'll learn about classes, objects, attributes, and methods. Classes are blueprints for creating objects, and objects are instances of classes.

## Key Concepts
- **Class**: A template for creating objects. It defines attributes (data) and methods (functions).
- **Object**: An instance of a class.
- **Attributes**: Variables that belong to a class or object.
- **Methods**: Functions defined inside a class.

## The Arch
Imagine "TheArch" as a class representing Noah's Ark. Each instance (object) could be a specific ark, like "noah_arch", with attributes like size, passengers, and methods like loading animals.

### Code Example
```python
class TheArch:
    def __init__(self, builder, size):
        self.builder = builder
        self.size = size
        self.passengers = []

    def load_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger} has boarded the ark.")

    def describe(self):
        return f"This ark was built by {self.builder}, size {self.size}, with passengers: {self.passengers}"

# Creating an instance (object)
noah_arch = TheArch("Noah", "300 cubits")
noah_arch.load_passenger("Noah")
noah_arch.load_passenger("Sheep")
print(noah_arch.describe())
```

## Exercises
1. Create a class for "Disciples" with attributes like name and role, and a method to introduce themselves.
2. Instantiate objects for disciples like Peter and John.