from urllib.parse import quote
from dateutil import parser

def iso_to_gcal(dt_str):
    # Google Calendar needs UTC or "floating" (no offset). Let's use UTC (Z)
    dt = parser.isoparse(dt_str)
    # Convert to UTC if not already
    dt_utc = dt.astimezone(tz=None).astimezone(tz=None).replace(tzinfo=None) if dt.tzinfo else dt
    return dt_utc.strftime('%Y%m%dT%H%M%SZ')

def create_google_calendar_link(event: dict) -> str:
    title = event.get("summary", "Event")
    start = iso_to_gcal(event.get("start", ""))
    end = iso_to_gcal(event.get("end", ""))
    details = event.get("description", "")
    location = event.get("location", "")

    base_url = "https://calendar.google.com/calendar/r/eventedit?"
    params = {
        "text": title,
        "dates": f"{start}/{end}",
        "details": details,
        "location": location,
        "trp": "false"
    }
    encoded = "&".join(f"{k}={quote(str(v))}" for k, v in params.items() if v)
    return base_url + encoded
