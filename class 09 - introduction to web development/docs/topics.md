# Class 9: Introduction to Web Development

## Overview
Build simple web apps with FastAPI.

## Key Concepts
- **Routes**: URL endpoints.
- **Templates**: HTML rendering.
- **Requests**: Handling user input.

##Gospel Website
A simple site displaying Bible verses.

### Code Example
```python
from fastapi import FastAPI, status

app = FastAPI(__name__)

@app.get("/")
def home():
    return "Welcome to the Gospel!"

@app.get("/verse/{book}", status_code=status.HTTP_200_OK)
def verse(book):
    verses = {"Genesis": "In the beginning..."}`
    return verses.get(book, "Verse not found")
```

## Exercises
1. Add a route for prayers.
2. Use templates for HTML.