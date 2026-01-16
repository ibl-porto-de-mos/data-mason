# Class 9: Introduction to Web Development

## Overview
Build simple web apps with Flask.

## Key Concepts
- **Routes**: URL endpoints.
- **Templates**: HTML rendering.
- **Requests**: Handling user input.

## Christian Example: Gospel Website
A simple site displaying Bible verses.

### Code Example
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Gospel!"

@app.route('/verse/<book>')
def verse(book):
    verses = {"Genesis": "In the beginning..."}
    return verses.get(book, "Verse not found")

if __name__ == '__main__':
    app.run()
```

## Exercises
1. Add a route for prayers.
2. Use templates for HTML.