from datetime import datetime, timezone
from dateutil import parser

# converts ISO-8601 datetime string to ICS format (YYYYMMDDTHHMMSS)
def iso_to_ics(dt_str):
    dt = parser.isoparse(dt_str)
    return dt.strftime('%Y%m%dT%H%M%S')

# converts event dict to ICS format string
def event_dict_to_ics(event: dict) -> str:
    summary = event.get("summary", "Event")
    description = event.get("description", "")
    location = event.get("location", "")
    organizer = event.get("organizer_name", "")
    organizer_email = event.get("organizer_email", "")
    start = event.get("start", "")
    end = event.get("end", "")
    tzid = event.get("timezone", "UTC")

    uid = f"{abs(hash(summary + start))}@text2isc"
    dtstamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    ics = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//text2isc//EN",
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{dtstamp}",
        f"DTSTART;TZID={tzid}:{iso_to_ics(start)}",
        f"DTEND;TZID={tzid}:{iso_to_ics(end)}",
        f"SUMMARY:{summary}",
        f"DESCRIPTION:{description}",
        f"LOCATION:{location}",
    ]
    if organizer and organizer_email:
        ics.append(f"ORGANIZER;CN={organizer}:MAILTO:{organizer_email}")
    ics.append("END:VEVENT")
    ics.append("END:VCALENDAR")

    return "\r\n".join(ics)
