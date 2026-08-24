from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "I keep dancing on my own!"}

