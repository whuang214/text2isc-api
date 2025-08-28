# text2isc

![text2isc Demo](https://i.imgur.com/WKeBB9P.png)

text2isc is a smart API that instantly transforms unstructured event announcements into ready-to-import calendar events—perfect for saving time and reducing manual entry.

**Deployed App:** https://text2isc.vercel.app/

**Frontend Repo:** https://github.com/whuang214/text2isc-client

## Why I Built This
- **Problem:** Adding events from emails or flyers to your calendar is tedious and error-prone.
- **Solution:** text2isc uses LLMs to extract details from raw event text, then generates ready-to-import ICS files or Google Calendar links in seconds.
- **My Role:** Designed and built the API and data pipeline from scratch (FastAPI, Python, Docker), including natural language parsing, data modeling, and integrations.

## What It Does
1. **Text → JSON:** Convert free-form event blurbs into structured JSON (summary, datetime, location, etc.)
2. **JSON → ICS:** Generate a downloadable `.ics` calendar file
3. **JSON → Google Calendar:** Produce a one-click Google Calendar event link
4. **Interactive API:** Explore endpoints via auto-generated OpenAPI docs at `/docs`

## Key Features
- **Universal Parsing:** Handles dates, times, timezones, locations, descriptions, and organizer info
- **Multi-format Output:** JSON, ICS, and Google Calendar link
- **Developer Friendly:** Dockerized with clear OpenAPI schema and robust error handling
- **Extensible & Portable:** Run locally with Python 3.10+ or in any container environment

## Tech Stack
| Layer      | Technology                    |
|------------|-------------------------------|
| Backend    | FastAPI (Python)              |
| AI         | OpenRouter LLMs               |
| Packaging  | Docker & Docker Compose       |
| Calendar   | ICS builder & link generator  |
| Frontend   | React (text2isc-client)       |
| Hosting    | Vercel (frontend), Heroku (API) |

## Recruiter Highlights
- **End-to-End Ownership:** From prompt engineering to deployment
- **LLM Integration:** Real-world text parsing powered by generative AI
- **Production-Ready:** Containerized, documented, and scalable
- **User-Centric:** Fast, accurate, and easy to integrate into any workflow
