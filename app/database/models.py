from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

Base = declarative_base()

class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    pregunta = Column(Text)

    respuesta = Column(Text)

    fecha = Column(DateTime, default=datetime.utcnow)