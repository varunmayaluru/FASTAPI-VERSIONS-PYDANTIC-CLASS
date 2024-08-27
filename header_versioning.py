from fastapi import FastAPI, Request, HTTPException, Header, Depends
from enum import Enum

app = FastAPI()

# Define an Enum for version numbers
class VersionNumber(str, Enum):
    v1 = "1"
    v2 = "2"

# Dependency to extract and pass the version header
def get_version_header(version: str = Header(...)):
    return version

# Define a simple endpoint with header versioning
@app.get("/items/")
async def get_items(version: str = Depends(get_version_header)):
    if version == VersionNumber.v1:
        return {"message": "This is version 1 of the API"}
    elif version == VersionNumber.v2:
        return {"message": "This is version 2 of the API"}
    else:
        raise HTTPException(status_code=400, detail="Unsupported API version")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
