from fastapi import FastAPI
from app.api.endpoints.chat import router as chat_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Medical Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router, prefix="/api/v1")

# Add these configuration variables to your settings.py
APP_HOST = "0.0.0.0"  # or "localhost"
APP_PORT = 8015       # or any other port you prefer

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)