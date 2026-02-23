from fastapi import APIRouter, UploadFile, File, HTTPException
from model.schema import ImageMetadata

route = APIRouter()


@route.post("/upload") 
async def upload_image(file: UploadFile = File(...)):
    try:
        print(f"Received file: {file.filename}")
        return {"status": "success", "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))