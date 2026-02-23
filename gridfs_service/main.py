from fastapi import FastAPI
from gridfs_router import route
import uvicorn

app = FastAPI()

app.include_router(route, prefix="/metadata")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)