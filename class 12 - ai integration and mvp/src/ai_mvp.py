from fastapi import FastAPI
import openai

app = FastAPI()
openai.api_key = "your-key"  # Replace with actual key

@app.get("/story/{theme}")
def generate_story(theme: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a short biblical story about {theme}",
        max_tokens=100
    )
    return {"story": response.choices[0].text.strip()}