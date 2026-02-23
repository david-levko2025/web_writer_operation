from fastapi import FastAPI, BackgroundTasks

from app.ingestion_orchestrator import IngestionOrchestrator
import uvicorn

app = FastAPI(title="Ingestion Service")
orchestrator = IngestionOrchestrator()

@app.post("/process")
async def start_processing(background_tasks: BackgroundTasks):
    background_tasks.add_task(orchestrator.run_pipeline)
    return {
            "status": "success", 
            "message": "bibeline started"
            }

@app.get("/health")
async def health_check():
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)