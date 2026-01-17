from fastapi import FastAPI
from core.orchestrator import Orchestrator
from core.memory import Memory

app = FastAPI()
orchestrator = Orchestrator(Memory())

@app.post("/create_course")
def create_course(domain: str):
    return orchestrator.create_course(domain)
