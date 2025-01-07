from fastapi import APIRouter, HTTPException, Request
from app.services.chatbot import ChatbotService
from app.models.schemas import ChatResponse, ErrorResponse

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: Request):
    try:
        data = await request.json()
        question = data.get('question')

        if not question:
            return {
                "detail": "Question is required"
            }, 400

        response = await chatbot_service.get_response(question)

        # Convert the response to our dataclass
        return {
            "answer": response["answer"],
            "sources": response["sources"]
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )