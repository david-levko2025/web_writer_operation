from pymongo import MongoClient
import gridfs
from gridfs_config import GridFSConfig

class GridFSStorage:
    def __init__(self, config: GridFSConfig):
        self.client = MongoClient(config.mongodb_uri)
        self.db = self.client[config.database_name]
        self.fs = gridfs.GridFS(self.db)

    def save_file(self, file_content: bytes, filename: str):
        return self.fs.put(file_content, filename=filename)
         