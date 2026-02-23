from pymongo import MongoClient
import os
import gridfs
from pymongo.errors import ConnectionFailure

class MongoConnector:
    def __init__(self):

        self.db_name = os.getenv("DATABASE_NAME", "image_db")
        self.mongo_url = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
        self.client = None
        self._db = None
        self._fs = None

    def get_client(self):
        if self.client is None:
            self.client = MongoClient(self.mongo_url)
        return self.client

    def get_db(self):
        if self._db is None:
            self._db = self.get_client()[self.db_name]
        return self._db

    def get_fs(self):
        if self._fs is None:
            self._fs = gridfs.GridFS(self.get_db())
        return self._fs

    def check_connection(self):
        try:
            client = self.get_client()
            client.admin.command('ping')
            print("successfully connected to mongodb")
            return True
        except ConnectionFailure as error:
            print(f"mongodb Server not available: {error}")
            return False

    def get_coll(self, coll_name):
        db = self.get_db()
        return db[coll_name]