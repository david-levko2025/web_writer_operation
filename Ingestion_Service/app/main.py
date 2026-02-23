import uvicorn
from fastapi import FastAPI
from route.router import route

app = FastAPI(debug=True)

app.include_router(route,prefix="/metadata")

@app.get("/health")
async def health_check():
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run("app.main:app",host="localhost",port=8000,reload=True)