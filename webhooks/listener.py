import os
import json
import subprocess
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Zero-Touch Crash Ingestor")

class ErrorPayload(BaseModel):
    environment: str
    repository: str
    error_message: str
    stack_trace: str

def auto_repair_pipeline(payload: ErrorPayload):
    """Executes the zero-touch fix loop in background."""
    print(f"\n[ENGINE] Initiating auto-repair for: {payload.error_message}")
    
    # 1. Save crash context for Bob Agent
    context = {
        "error": payload.error_message,
        "traceback": payload.stack_trace,
        "suggested_file": "app/calculator.py"
    }
    with open("incident_context.json", "w") as f:
        json.dump(context, f, indent=2)

    # 2. Verify current failure baseline via PyTest
    test_run = subprocess.run(["pytest", "tests/"], capture_output=True, text=True)
    if test_run.returncode == 0:
        print("[ENGINE] System is currently healthy. No fix needed.")
        return

    # 3. Create an isolated git repair branch
    branch_id = os.urandom(3).hex()
    branch_name = f"fix/auto-repair-{branch_id}"
    subprocess.run(["git", "checkout", "-b", branch_name])
    print(f"[GIT] Created feature branch: {branch_name}")

    # 4. Trigger Headless / Scripted Repair Directive
    # Note: During the hackathon, you can execute the Bob Agent prompt directly 
    # in Bob IDE based on `incident_context.json` to preserve Bobcoins efficiently.
    print("[ENGINE] Crash context generated in `incident_context.json`. Ready for agent processing.")

@app.post("/webhook/error", status_code=202)
async def receive_crash_log(payload: ErrorPayload, background_tasks: BackgroundTasks):
    if not payload.error_message:
        raise HTTPException(status_code=400, detail="Invalid payload")
        
    print(f"[CRASH INGESTED] {payload.error_message} from {payload.environment}")
    
    # Trigger non-blocking repair task
    background_tasks.add_task(auto_repair_pipeline, payload)
    
    return {
        "status": "ingested",
        "action": "auto_repair_triggered",
        "incident_file": "incident_context.json"
    }