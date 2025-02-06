from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    print("Someone pinged this API.")
    print("DEEPSEEK_API_KEY:", os.getenv("DEEPSEEK_API_KEY"))
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
