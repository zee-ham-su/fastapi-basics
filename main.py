from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def _root():
    return {"Hello": "World"}