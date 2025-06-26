from fastapi import APIRouter
from app.core.isc_converter import convert_text_to_isc

router = APIRouter()

# isc root endpoint
@router.get("/")
async def root():
    # print("OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))
    return {"message": "Hello from ISC API!"}

# isc/convert endpoint
@router.get("/convert")
async def root():
    output = convert_text_to_isc("What is the meaning of life?") # call the convert_text_to_isc function with a sample text
    return {"message": f"{output}"}
