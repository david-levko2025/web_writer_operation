from fastapi import UploadFile
from gridfs_storage import GridFSStorage

class GridFSOrchestrator:
    def __init__(self, storage: GridFSStorage):
        self.storage = storage

    async def handle_upload(self, file: UploadFile):
        content = await file.read()
        file_id = self.storage.save_file(content, file.filename)  # type: ignore
        return file_id