from fastapi import APIRouter
from app.core.isc_converter import convert_text_to_isc
import os

router = APIRouter()

# isc/ro
@router.get("/")
async def root():
    # print("OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))
    return {"message": "Hello from ISC API!"}
