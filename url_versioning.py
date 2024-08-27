from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/v1/hello")
async def hello_v1():
    return {"message": "Hello, World! This is version 1"}

@app.get("/v2/hello")
async def hello_v2():
    return {"message": "Hello, World! This is version 2"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
