# Class 2: Control Structures

## Overview
Control structures allow us to make decisions and repeat actions in our code. This includes conditional statements (if/else) and loops (for/while).

## Key Concepts
- **If/Else**: Execute code based on conditions.
- **For Loop**: Iterate over sequences.
- **While Loop**: Repeat while a condition is true.

##Counting Disciples
Imagine checking a list of disciples and greeting them based on their role, or looping through the Ten Commandments.

### Code Example
```python
disciples = ["Peter", "John", "Mary", "Paul"]

# If/else example
for disciple in disciples:
    if disciple == "Paul":
        print(f"{disciple} is an apostle!")
    else:
        print(f"Hello, {disciple}!")

# While loop example
commandments = ["Honor God", "Love thy neighbor", "Do not steal"]
i = 0
while i < len(commandments):
    print(f"Commandment {i+1}: {commandments[i]}")
    i += 1
```

## Exercises
1. Use if/else to check if a number is even or odd, like checking "days of creation".
2. Loop through a list of parables and print them.