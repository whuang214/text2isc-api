from pydantic import BaseModel, validator

# Request model to validate input JSON
class TextInput(BaseModel):
    event_details: str
    
    @validator('event_details')
    def not_empty(cls, v):
        if not v.strip():
            raise ValueError('event_details cannot be empty')
        return v
    
# event model to represent extracted event data
class EventData(BaseModel):
    summary: str
    start: str
    end: str
    timezone: str
    location: str
    description: str
    organizer_name: str
    organizer_email: str
