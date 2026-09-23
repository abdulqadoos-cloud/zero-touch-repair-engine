from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Zero-Touch Crash Ingestor")

class ErrorPayload(BaseModel):
    environment: str
    repository: str
    error_message: str
    stack_trace: str

@app.post("/webhook/error")
async def receive_crash_log(payload: ErrorPayload):
    print(f"[CRASH RECEIVED] {payload.error_message}")
    # This payload will be passed into IBM Bob 2.0 to trigger the repair loop
    return {"status": "ingested", "bug": payload.error_message}