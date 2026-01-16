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