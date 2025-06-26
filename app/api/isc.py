from fastapi import APIRouter
from pydantic import BaseModel, validator
from app.core.isc_converter import convert_text_to_isc

router = APIRouter()

# Request model to validate input JSON
class TextInput(BaseModel):
    event_details: str
    
    @validator('event_details')
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError('event_details cannot be empty')
        return v
    

# isc root endpoint
@router.get("/")
async def root():
    return {"message": "Hello from ISC API!"}

# isc/convert endpoint, accepts POST with JSON body containing 'text'
@router.post("/convert")
async def convert(input: TextInput):
    output = convert_text_to_isc(input.event_details)
    return {"isc_data": output}
