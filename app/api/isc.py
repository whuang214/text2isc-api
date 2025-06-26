from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/")
async def root():
    # print("OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))
    return {"message": "Hello from ISC API!"}
