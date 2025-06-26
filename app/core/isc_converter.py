from openai import OpenAI
import os

# Initialize OpenAI client with OpenRouter endpoint and API key from environment variable
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def convert_text_to_isc(event_text: str) -> str:
    print(f"String to convert: {event_text}")
    SYSTEM_PROMPT = {
            "role": "system",
            "content": "You are an expert calendar assistant. \
Convert the user’s raw event text into a **single-event** RFC 5545-compliant iCalendar file (.ics). \
Follow these rules:\n\n\
1. **Output ONLY valid ICS lines** – no markdown, comments, or extra prose.\n\
2. Wrap everything between BEGIN:VCALENDAR and END:VCALENDAR. \
Use VERSION:2.0 and PRODID:-//text2isc//EN.\n\
3. Inside BEGIN:VEVENT … END:VEVENT include at minimum:\n\
   • UID: a deterministic UUID (hash the SUMMARY + DTSTART).\n\
   • DTSTAMP: current UTC time in yyyymmddThhmmssZ.\n\
   • DTSTART / DTEND: derive from the text. \
     – If only a start time is given, set DTEND 1 hour later. \
     – Use the TZID if a city or time zone is mentioned (e.g. “America/New_York”); \
       otherwise default to UTC.\n\
   • SUMMARY: short event title.\n\
   • DESCRIPTION: full body, escaped for ICS (\, \\n, ;, , where needed).\n\
   • LOCATION: street + city + country if available.\n\
   • ORGANIZER;CN=Name:MAILTO:email@example.com – if an organizer is mentioned; else omit.\n\
4. Preserve line length ≤ 75 bytes; fold long lines per RFC 5545 (CRLF + single space).\n\
5. Use CRLF (\\r\\n) line endings.\n\
6. After END:VEVENT close with END:VCALENDAR.\n\n\
Return **only** the finished ICS file.",
        }
    messages = [
    SYSTEM_PROMPT,
    {
        "role": "user",
        "content": event_text   # the raw announcement you receive
    }
]


    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528-qwen3-8b:free",  # any model from https://openrouter.ai/models
        messages=messages,
        extra_headers={
            # for tracking purposes
            # "HTTP-Referer": "your-site-url.com",
            "X-Title": "text2isc",
        },
    )

    isc_data = completion.choices[0].message.content
    return isc_data
