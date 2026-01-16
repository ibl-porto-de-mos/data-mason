# Class 11: Building APIs

## Overview
Create REST APIs with FastAPI.

## Key Concepts
- **Endpoints**: API routes.
- **Pydantic**: Data validation.
- **Async**: Asynchronous operations.

##Prayer API
API for submitting and retrieving prayers.

### Code Example
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prayer(BaseModel):
    content: str
    author: str

prayers = []

@app.post("/pray")
def submit_prayer(prayer: Prayer):
    prayers.append(prayer)
    return {"message": "Prayer submitted"}

@app.get("/prayers")
def get_prayers():
    return prayers
```

## Exercises
1. Add a delete endpoint.
2. Validate prayer content.