# Class 8: Advanced Python Features

## Overview
Decorators, generators, and comprehensions for efficient code.

## Key Concepts
- **Decorators**: Modify functions.
- **Generators**: Yield values lazily.
- **Comprehensions**: Concise list/dict creation.

##Blessings
Use decorators for prayers, generators for counting blessings.

### Code Example
```python
# Decorator
def prayer(func):
    def wrapper(*args, **kwargs):
        print("Amen!")
        return func(*args, **kwargs)
    return wrapper

@prayer
def preach():
    print("Love thy neighbor")

# Generator
def count_blessings(n):
    for i in range(n):
        yield f"Blessing {i+1}"

# Comprehension
disciples = [d.upper() for d in ["peter", "john"]]
```

## Exercises
1. Create a decorator for logging actions.
2. Use a generator for Bible verses.