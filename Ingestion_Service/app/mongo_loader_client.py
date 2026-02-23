import requests
import os

class MongoLoaderClient:
    def __init__(self, loader_url):
        self.loader_url = loader_url

    def forward_binary(self, image_path):
        try:
            with open(image_path, "rb") as f:
                files = {"file": (os.path.basename(image_path), f, "image/png")}
                response = requests.post(self.loader_url, files=files)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"loader Client Error: {e}")
            return None