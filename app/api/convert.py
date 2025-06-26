from fastapi import APIRouter, Response
import re

from app.core.event_converter import convert_text_to_event
from app.utils.isc_builder import event_dict_to_ics
from app.model.event import TextInput, EventData

router = APIRouter()

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
async def event_json_to_ics(event: EventData):
    ics_content = event_dict_to_ics(event.dict())
    summary = event.summary or "event"
    safe_summary = re.sub(r'[^\w\-]', '_', summary).strip('_')[:50]
    filename = f"{safe_summary or 'event'}.ics"
    return Response(
        content=ics_content,
        media_type="text/calendar",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )
