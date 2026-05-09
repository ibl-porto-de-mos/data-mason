from fastapi import FastAPI, status

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to the Gospel!"

@app.get("/verse/{book}", status_code=status.HTTP_200_OK)
def verse(book):
    verses = {"Genesis": "In the beginning..."}
    return verses.get(book, "Verse not found")
