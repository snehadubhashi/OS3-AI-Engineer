from fastapi import FastAPI

from app.api import router

app = FastAPI(
    title="Production LangGraph Agent API",
    version="2.0.0"
)

app.include_router(router)


@app.get("/")
async def home():
    return {
        "status": "Running"
    }