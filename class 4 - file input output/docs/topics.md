# Class 4: File Input/Output

## Overview
Learn to read from and write to files, essential for data persistence.

## Key Concepts
- **Opening Files**: Use `open()` with modes like 'r', 'w'.
- **Reading**: `read()`, `readlines()`.
- **Writing**: `write()`.
- **Closing**: Always close files or use `with`.

## Christian Example: Saving Scriptures
Read and write Bible verses to files.

### Code Example
```python
# Writing to a file
with open("scriptures.txt", "w") as file:
    file.write("In the beginning, God created the heavens and the earth.\n")
    file.write("For God so loved the world...\n")

# Reading from a file
with open("scriptures.txt", "r") as file:
    content = file.read()
    print(content)
```

## Exercises
1. Write a list of commandments to a file.
2. Read and display parables from a file.