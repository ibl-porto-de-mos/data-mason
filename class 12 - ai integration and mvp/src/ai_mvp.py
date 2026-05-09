import os

from fastapi import FastAPI
from openrouter import OpenRouter

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]

app = FastAPI()

@app.get("/story/{theme}")
def generate_story(theme: str):

    with OpenRouter(api_key=OPENROUTER_API_KEY) as client:
        response = client.chat.send(
            model= "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
            messages=[
                {"role": "user", "content":  f"Escreva uma curta história bíblica sobre o tema: {theme}"}
            ],
        )

    return {"story": response.choices[0].message.content}
