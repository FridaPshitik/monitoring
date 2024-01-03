from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/print")
async def root():
    return {"message-print": "Hello, World print!"}