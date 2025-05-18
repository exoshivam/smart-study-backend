from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.scheduler import generate_schedule

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate_schedule")
async def create_schedule(request: Request):
    data = await request.json()
    schedule = generate_schedule(data)
    return {"schedule": schedule}
