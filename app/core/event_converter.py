from openai import OpenAI
import os, json

# Initialize OpenAI client with OpenRouter endpoint and API key from environment variable
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

SYSTEM_PROMPT = {
  "role": "system",
  "content": "You are an expert event-parser.\n\
Convert the user’s raw announcement into a single JSON object with the exact keys listed below – **no extra keys, no comments, no markdown**.\n\n\
####################  REQUIRED OUTPUT FORMAT  ####################\n\
{\n\
  \"summary\":        \"<Short event title>\",\n\
  \"start\":          \"<ISO-8601 datetime with offset, e.g. 2025-05-30T17:30:00-04:00>\",\n\
  \"end\":            \"<ISO-8601 datetime with offset>\",\n\
  \"timezone\":       \"<IANA TZ ID, e.g. America/New_York or UTC>\",\n\
  \"location\":       \"<Street, City, Region, Country>\",\n\
  \"description\":    \"<Full description, single line with \\n for breaks>\",\n\
  \"organizer_name\": \"<Name if present, else \"\">\",\n\
  \"organizer_email\":\"<Email if present, else \"\">\"\n\
}\n\
#################################################################\n\n\
RULES & HEURISTICS:\n\
1. **summary** → First clear event title (strip greeting lines like \"Dear …\").\n\
2. **Dates / times** →\n\
   • Parse any date formats (e.g. “May 30, 2025”, “30/05/25”, “05-30-25”).\n\
   • Parse times like “5:30 PM – 10 PM”, “17:00-18:30”, “all day”.\n\
   • If only a start time exists, set **end** = start + 1 hour.\n\
   • If no time is given, treat it as an **all-day** event starting at 00:00 local time; set **end** = start + 1 day.\n\
3. **timezone** →\n\
   • If the text names a city/zone (e.g. “America, New York”, “CEST”, “PST”), map it to a valid IANA TZ ID (e.g. America/New_York, Europe/Berlin).\n\
   • Else default to \"UTC\" and make start/end ISO strings ending with \"Z\".\n\
4. **location** → Concatenate street, city, region, country if present; else \"\".\n\
5. **description** → Remainder of the announcement (remove boilerplate like footer notices). Escape internal newlines as \\n.\n\
6. **organizer_name/email** → Extract if clearly present (e.g. \"John Fleming <john@x.com>\"). If none, return empty strings.\n\
7. Trim whitespace, convert multiple spaces to single spaces. Do **not** include line breaks except inside description (escaped \\n).\n\
8. Output must be valid JSON (double quotes, no trailing commas) **and nothing else**."
}

# converts 
def convert_text_to_event(event_text: str) -> dict:
    # print(f"String to convert: {event_text}")

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

    json_str = completion.choices[0].message.content
    event_data = json.loads(json_str)
    return event_data
