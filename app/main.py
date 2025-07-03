import os
from fastapi import FastAPI
from app.api import convert
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

is_production = os.getenv("PRODUCTION") == "true"
frontend_url = os.getenv("FRONT_END_URL")

allowed_origins = [frontend_url] if is_production and frontend_url else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["content-disposition"]
)

# router for ISC API
app.include_router(convert.router, prefix="/convert", tags=["convert"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
