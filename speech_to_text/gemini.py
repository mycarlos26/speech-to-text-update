import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

class Gemini:
    def __init__(self):
        # Configurar la API de Gemini con la clave de entorno
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise EnvironmentError("GEMINI_API_KEY environment variable not found.")
        genai.configure(api_key=api_key)
        
        # Definir parámetros del modelo
        self.MODEL_NAME = "gemini-2.0-flash-exp"
        self.MAX_TOKENS = 8192  # Equivalente al parámetro original de max_output_tokens

        # Configuración de generación del modelo
        self.generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": self.MAX_TOKENS,
            "response_mime_type": "text/plain",
        }

        self.system_instruction = (
            "You are an experienced Quality Assurance (QA) professional with expertise in manual and automated testing. "
            "Provide brief, to-the-point answers to interview questions, focusing on practical applications and industry best practices. "
            "Keep responses concise and limited to key insights without additional details."
        )
    def text_proofreading(self, text: str) -> str:
        """Genera una respuesta basada en el texto de entrada utilizando el modelo de Gemini."""
        model = genai.GenerativeModel(
            model_name=self.MODEL_NAME,
            generation_config=self.generation_config,
            system_instruction=self.system_instruction,
        )
        
        # Iniciar sesión de chat y enviar el mensaje
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(text)
        
        return response.text.strip()
