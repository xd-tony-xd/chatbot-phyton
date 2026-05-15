from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def preguntar_ia(mensaje):

    respuesta = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": """
                Eres StarTraining AI.

                Ayudas a estudiantes universitarios
                a encontrar prácticas preprofesionales.

                Respondes claro y profesional.
                """
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]
    )

    return respuesta.choices[0].message.content