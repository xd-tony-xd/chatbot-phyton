from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.groq_service import preguntar_ia

from app.database.connection import SessionLocal
from app.database.models import Conversation

router = APIRouter()

@router.post("/chat")
def chat(data: ChatRequest):

    respuesta = preguntar_ia(data.mensaje)

    db = SessionLocal()

    nueva_conversacion = Conversation(
        pregunta=data.mensaje,
        respuesta=respuesta
    )

    db.add(nueva_conversacion)

    db.commit()

    db.close()

    return {
        "respuesta": respuesta
    }