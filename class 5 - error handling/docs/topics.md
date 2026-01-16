# Class 5: Error Handling

## Overview
Handle errors gracefully using try/except blocks.

## Key Concepts
- **Try/Except**: Catch exceptions.
- **Finally**: Always execute.
- **Raise**: Throw custom errors.

## Christian Example: Handling Temptation
Simulate errors like "temptation" and handle them.

### Code Example
```python
try:
    disciples = ["Peter", "John"]
    print(disciples[2])  # IndexError
except IndexError:
    print("Temptation avoided: Stay within bounds!")
finally:
    print("Always pray for guidance.")
```

## Exercises
1. Handle division by zero like avoiding "sin".
2. Raise a custom error for invalid inputs.