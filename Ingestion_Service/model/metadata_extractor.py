import os
import uuid
from PIL import Image

class MetadataExtractor:
    def extract(self, image_path: str) -> dict:
        try:
            with Image.open(image_path) as img:
                return {
                    "image_id": str(uuid.uuid4()),
                    "format": img.format,
                    "dimensions": {"width": img.width, "height": img.height},
                    "size_bytes": os.path.getsize(image_path)
                }
        except Exception as e:
            print(f"metadata Error: {e}")
            return {"image_id": str(uuid.uuid4())}