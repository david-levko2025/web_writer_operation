from fastapi import APIRouter, UploadFile, File
from gridfs_orchestrator import GridFSOrchestrator
from gridfs_storage import GridFSStorage
from gridfs_config import GridFSConfig

route = APIRouter()


config = GridFSConfig()
storage = GridFSStorage(config)
orchestrator = GridFSOrchestrator(storage)

@route.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_id = await orchestrator.handle_upload(file)
    return {
            "status": "success", 
            "mongodb_id": str(file_id)
            }