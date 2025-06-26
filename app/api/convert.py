from fastapi import APIRouter, Response
from pydantic import BaseModel, validator
import re

from app.core.event_converter import convert_text_to_event
from app.utils.isc_builder import event_dict_to_ics

router = APIRouter()

# Request model to validate input JSON
class TextInput(BaseModel):
    event_details: str
    
    @validator('event_details')
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError('event_details cannot be empty')
        return v

# convert root endpoint
@router.get("/")
async def root():
    return {"message": "Hello from convert route!"}

# just to test JSON output
@router.post("/json")
async def convert_to_json(input: TextInput):
    event_data = convert_text_to_event(input.event_details)
    return event_data

# convert endpoint to convert text to ISC
@router.post("/isc")
async def convert(input: TextInput):
    # Step 1: get event dict
    event_data = convert_text_to_event(input.event_details)
    # Step 2: build .ics string
    ics_content = event_dict_to_ics(event_data)
    # Step 3: get safe filename
    summary = event_data.get("summary", "event")
    safe_summary = re.sub(r'[^\w\-]', '_', summary).strip('_')[:50]
    filename = f"{safe_summary or 'event'}.ics"

    return Response(
        content=ics_content,
        media_type="text/calendar",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        }
    )