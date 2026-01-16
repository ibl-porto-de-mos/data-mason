# Class 7: Inheritance and Polymorphism

## Overview
Advanced OOP: Inherit from classes and override methods.

## Key Concepts
- **Inheritance**: Child classes inherit from parents.
- **Polymorphism**: Same method, different behavior.

## Christian Example: Prophets
Base class "Prophet", subclasses like "Moses" and "Elijah".

### Code Example
```python
class Prophet:
    def speak(self):
        return "Hear the word of God!"

class Moses(Prophet):
    def speak(self):
        return "Let my people go!"

class Elijah(Prophet):
    def speak(self):
        return "Fire from heaven!"

prophets = [Moses(), Elijah()]
for p in prophets:
    print(p.speak())
```

## Exercises
1. Create a "Disciple" base class with subclasses.
2. Demonstrate polymorphism.