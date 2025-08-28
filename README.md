# text2isc

![text2isc Demo](https://i.imgur.com/WKeBB9P.png)

text2isc is a smart API that instantly transforms unstructured event announcements into ready-to-import calendar events—perfect for saving time and reducing manual entry.

**Deployed App:** https://text2isc.vercel.app/

**Frontend Repo:** https://github.com/whuang214/text2isc-client

## Routes

### 1. POST `/json`
Convert free-form text into structured JSON.

**Example Request**
```json
{ "event_details": "Dinner with Sam next Tue 7pm at Row 34, Boston" }
```

**Example Reponse**
```json
{
  "summary": "Dinner with Sam",
  "start": "2025-09-02T19:00:00-04:00",
  "end": "2025-09-02T20:30:00-04:00",
  "location": "Row 34, Boston"
}
```

### 2. POST `/isc`
Generate a downloadable .ics calendar file from JSON.

**Example Request**
```
{
  "summary": "Team Meeting",
  "start": "2025-09-03T10:00:00-04:00",
  "end": "2025-09-03T11:00:00-04:00",
  "location": "Zoom",
  "description": "Sprint planning"
}
```

**Example Response**

Content-Type: `text/calendar`
Download: `Team_Meeting.ics`

### 3. POST `/google_calendar`

Create a one-click Google Calendar event link.

**Example Request**
```json
{
  "summary": "Team Meeting",
  "start": "2025-09-03T10:00:00-04:00",
  "end": "2025-09-03T11:00:00-04:00",
  "location": "Zoom",
  "description": "Sprint planning"
}
```

**Example Response**

```json
{
  "google_calendar_link": "https://calendar.google.com/calendar/render?...Team+Meeting..."
}
```

## Why I Built This
- **Problem:** Adding events from emails or flyers to your calendar is tedious and error-prone.
- **Solution:** text2isc uses LLMs to extract details from raw event text, then generates ready-to-import ICS files or Google Calendar links in seconds.

## Tech Stack
| Layer      | Technology                    |
|------------|-------------------------------|
| Backend    | FastAPI (Python)              |
| AI         | OpenRouter LLMs               |
| Packaging  | Docker & Docker Compose       |
| Calendar   | ICS builder & link generator  |
| Frontend   | React (text2isc-client)       |
| Hosting    | Vercel (frontend), Heroku (API) |
