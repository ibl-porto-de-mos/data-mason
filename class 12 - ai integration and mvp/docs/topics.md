# Class 12: AI Integration and MVP

## Overview
Build an MVP FastAPI app with AI for generating biblical stories.

## Key Concepts
- **AI Integration**: Use OpenAI API for text generation.
- **MVP**: Minimum Viable Product with core features.

##Biblical Story Generator
API that generates stories based on themes.

### Code Example
```python
from fastapi import FastAPI
import openai

app = FastAPI()
openai.api_key = "your-key"

@app.get("/story/{theme}")
def generate_story(theme: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a short biblical story about {theme}",
        max_tokens=100
    )
    return {"story": response.choices[0].text.strip()}
```

## Exercises
1. Add user authentication.
2. Deploy the app.