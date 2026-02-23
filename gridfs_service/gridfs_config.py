import os

class GridFSConfig:
    def __init__(self):
        self.mongodb_uri = os.getenv("MONGODB_URI", "mongodb://127.0.0.1:27017/")
        self.database_name = os.getenv("DATABASE_NAME", "image_db")
        self.collection_name = os.getenv("COLLECTION_NAME", "images")