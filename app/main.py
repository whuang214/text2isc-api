from fastapi import FastAPI
import os
from app.api import convert 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the main API!"}

# router for ISC API
app.include_router(convert.router, prefix="/convert", tags=["convert"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
