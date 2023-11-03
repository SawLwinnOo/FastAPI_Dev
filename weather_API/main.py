from fastapi import FastAPI
from app.api.endpoints import weather

app = FastAPI()

app.include_router(weather.router, prefix="/weather")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
