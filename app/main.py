from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router

from app.database.connection import engine
from app.database.models import Base

# crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="StarTraining ChatBot API"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rutas
app.include_router(chat_router)