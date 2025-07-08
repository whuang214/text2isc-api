import os
from fastapi import FastAPI
from app.api import convert
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

is_production = os.getenv("PRODUCTION", "").lower() == "true"
frontend_url = os.getenv("FRONT_END_URL")

print(f"PRODUCTION: {os.getenv('PRODUCTION')}")
print(f"is_production: {is_production}")
print(f"FRONT_END_URL: {frontend_url}")

if is_production:
    if not frontend_url:
        raise ValueError("FRONT_END_URL must be set in production")
    allowed_origins = [frontend_url]
else:
    allowed_origins = ["*"]

print(f"Allowed origins: {allowed_origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"]
)

app.include_router(convert.router, prefix="/convert", tags=["convert"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
