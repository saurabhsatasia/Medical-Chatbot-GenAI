from fastapi import APIRouter, Depends
from app.services.chatbot import ChatbotService
from app.models.schemas import ChatResponse

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat", response_model=ChatResponse)
async def chat(question: str) -> ChatResponse:
    return await chatbot_service.get_response(question)