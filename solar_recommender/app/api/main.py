from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Solar Recommendation Platform API",
    description="The API for the solar recommendation system, powered by a multi-agent architecture.",
    version="0.1.0",
)

from .endpoints import chat

app.include_router(chat.router, prefix="/api/v1", tags=["chat"])

@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to the Solar Recommendation Platform API!"}
