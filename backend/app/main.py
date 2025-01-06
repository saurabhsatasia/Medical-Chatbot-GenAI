from fastapi import FastAPI
from app.api.endpoints.chat import router as chat_router
import uvicorn

app = FastAPI(title="Medical Chatbot API")

# Include routers
app.include_router(chat_router, prefix="/api/v1")

# Add these configuration variables to your settings.py
APP_HOST = "0.0.0.0"  # or "localhost"
APP_PORT = 8000       # or any other port you prefer

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)