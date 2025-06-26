# text2isc
Turns unstructured event announcements into ready-to-import calendar events.

## Overview
text2isc is a FastAPI-based service that converts natural-language event descriptions into structured calendar formats (JSON, ICS), or generates a Google Calendar link. 

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- An OpenRouter API key (set `OPENROUTER_API_KEY` in your environment or docker-compose file)

## Quick Start (with Docker Compose)

1. **Clone the repo**

    ```
    git clone https://github.com/whuang214/text2isc.git
    cd text2isc
    ```

2. **Set your API key**

    Edit or create a `.env` file in the project root:

    ```
    OPENROUTER_API_KEY=<our_openrouter_api_key_here>
    ```

3. **Run with Docker Compose**

    ```
    docker-compose up --build
    ```

    The service will start on port 8000. Visit `http://localhost:8000/docs` for the interactive API docs.

## How to Use

### 1. Convert Free-Form Text → JSON

Original Event Text:
```
Boston Tech Meetup: Summer Networking at District Hall Boston, 75 Northern Ave, Boston, MA on July 18, 2025, 6:00pm – 9:30pm. Join local developers, founders, and tech professionals for a fun evening of networking, light snacks, and drinks. Don't miss our guest speaker, Sarah Lin, CEO of FutureAI, sharing insights on building products with generative AI.

Agenda:

- 6:00–6:45pm: Networking & refreshments
- 6:45–7:30pm: Guest talk – "Building with Generative AI"
- 7:30–9:30pm: Open mingling

Organizer: John Smith john.smith@example.com
```

- **Endpoint:** `POST /convert/json`
- **Request Body (after parsing):**
    ```
    {
    "event_details": "Boston Tech Meetup: Summer Networking at District Hall Boston, 75 Northern Ave, Boston, MA on July 18, 2025, 6:00pm – 9:30pm. Join local developers, founders, and tech professionals for a fun evening of networking, light snacks, and drinks. Don't miss our guest speaker, Sarah Lin, CEO of FutureAI, sharing insights on building products with generative AI.\n\nAgenda:\n- 6:00–6:45pm: Networking & refreshments\n- 6:45–7:30pm: Guest talk – \"Building with Generative AI\"\n- 7:30–9:30pm: Open mingling\n\nOrganizer: John Smith <john.smith@example.com>"
    }
    ```
- **Response Example:**
    ```
    {
    "summary": "Boston Tech Meetup: Summer Networking",
    "start": "2025-07-18T18:00:00-04:00",
    "end": "2025-07-18T21:30:00-04:00",
    "timezone": "America/New_York",
    "location": "District Hall Boston, 75 Northern Ave, Boston, MA 02210",
    "description": "Join local developers, founders, and tech professionals for a fun evening of networking, light snacks, and drinks. Don't miss our guest speaker, Sarah Lin, CEO of FutureAI, sharing insights on building products with generative AI.\n\nAgenda:\n- 6:00–6:45pm: Networking & refreshments\n- 6:45–7:30pm: Guest talk – \"Building with Generative AI\"\n- 7:30–9:30pm: Open mingling",
    "organizer_name": "John Smith",
    "organizer_email": "john.smith@example.com"
    }
    ```

### 2. Convert JSON → ICS

- **Endpoint:** `POST /convert/isc`
- **Request Body:** Use the above JSON (schema: summary, start, end, timezone, location, description, organizer_name, organizer_email)
- **Response:** Returns an ICS calendar file for download

### 3. Convert JSON → Google Calendar Link

- **Endpoint:** `POST /convert/google_calendar`
- **Request Body:** Same JSON as above
- **Response Example:**
    ```
    {
    "google_calendar_link": "https://calendar.google.com/calendar/r/eventedit?text=Boston+Tech+Meetup%3A+Summer+Networking&dates=20250718T220000Z%2F20250719T013000Z&details=Join+local+developers%2C+founders%2C+and+tech+professionals+for+a+fun+evening+of+networking%2C+light+snacks%2C+and+drinks.+Don%27t+miss+our+guest+speaker%2C+Sarah+Lin%2C+CEO+of+FutureAI%2C+sharing+insights+on+building+products+with+generative+AI.%5Cn%5CnAgenda%3A%5Cn-+6%3A00%E2%80%936%3A45pm%3A+Networking+%26+refreshments%5Cn-+6%3A45%E2%80%937%3A30pm%3A+Guest+talk+%E2%80%93+%22Building+with+Generative+AI%22%5Cn-+7%3A30%E2%80%939%3A30pm%3A+Open+mingling&location=District+Hall+Boston%2C+75+Northern+Ave%2C+Boston%2C+MA+02210"
    }
    ```

## API Routes

- `POST /convert/json`             → Convert free-form text to structured event JSON
- `POST /convert/isc`              → Convert event JSON to downloadable `.ics` file
- `POST /convert/google_calendar`  → Convert event JSON to Google Calendar link

Open [http://localhost:8000/docs](http://localhost:8000/docs) for a full interactive API playground.

## Project Structure

- `app/main.py` – FastAPI entrypoint
- `app/api/convert.py` – API route handlers
- `app/core/event_converter.py` – LLM-powered text to event parsing
- `app/model/event.py` – Data models
- `app/utils/isc_builder.py` – ICS generator
- `app/utils/calendar_links.py` – Google Calendar link generator