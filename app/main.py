from fastapi import FastAPI

from app.routes.chat import router as chat_router

from app.database.connection import engine
from app.database.models import Base

# crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StarTraining ChatBot API"
)

app.include_router(chat_router)