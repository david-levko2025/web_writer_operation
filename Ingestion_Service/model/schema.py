from pydantic import BaseModel

class ImageMetadata(BaseModel):
    image_id: str
    filename: str
    size_bytes: int
    dimensions: str 
    format: str     

class ImageProcessResult(BaseModel):
    image_id: str
    text: str
    metadata: ImageMetadata 