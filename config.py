"""
Configuración segura de API Keys
Carga variables desde .env
"""

import os
from dotenv import load_dotenv
from google import genai

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener API Keys desde variables de entorno
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'models/gemini-2.5-flash')  # Valor por defecto

def verify_keys():
    """Verifica que todas las API Keys estén configuradas"""
    
    if not GEMINI_API_KEY:
        raise ValueError(
            "❌ GEMINI_API_KEY no encontrada.\n"
            "Crea un archivo .env en la raíz del proyecto con:\n"
            "GEMINI_API_KEY=tu_api_key_aqui"
        )
    
    if not OPENWEATHER_API_KEY:
        raise ValueError(
            "❌ OPENWEATHER_API_KEY no encontrada.\n"
            "Agrega en el archivo .env:\n"
            "OPENWEATHER_API_KEY=tu_api_key_aqui"
        )
    
    print("✅ API Keys cargadas correctamente desde .env")
    return True

def get_gemini_client():
    """
    Retorna un cliente de Gemini configurado
    
    Returns:
        genai.Client: Cliente configurado de Gemini
    """
    verify_keys()
    return genai.Client(api_key=GEMINI_API_KEY)

# Ejecutar verificación si se corre directamente
if __name__ == "__main__":
    verify_keys()
    print(f"✅ Modelo Gemini configurado: {GEMINI_MODEL}")
    
    # Test rápido
    try:
        client = get_gemini_client()
        print("✅ Cliente Gemini inicializado correctamente")
    except Exception as e:
        print(f"❌ Error al inicializar Gemini: {e}")