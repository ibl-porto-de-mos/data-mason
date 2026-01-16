# Class 6: Modules and Packages

## Overview
Organize code into reusable modules and packages.

## Key Concepts
- **Module**: A .py file with functions/classes.
- **Package**: A directory with __init__.py.
- **Import**: Bring in modules.

## Christian Example: Gospel Module
Create a module for Bible-related functions.

### Code Example
```python
# In gospel.py
def preach(message):
    return f"Gospel: {message}"

# In main script
from gospel import preach
print(preach("Love one another"))
```

## Exercises
1. Create a module for prayer functions.
2. Import and use it in another script.