# ai-automation-portfolio
AI and automation projects using Python and Gemini

## 🚀 Setup / Instalación

### Prerrequisitos

- Python 3.10 o superior
- Cuenta de Gmail (para Gemini API)
- Git instalado

### Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/TU_USUARIO/ai-automation-portfolio.git
cd ai-automation-portfolio
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar API Keys:**

Crea un archivo `.env` en la raíz del proyecto (copia desde `.env.example`):
```bash
# Windows
copy .env.example .env

# Mac/Linux  
cp .env.example .env
```

Edita `.env` y agrega tus API Keys reales:
```env
GEMINI_API_KEY=tu_api_key_real_de_gemini
OPENWEATHER_API_KEY=tu_api_key_real_de_openweather
GEMINI_MODEL=models/gemini-2.5-flash
```

**📝 Cómo obtener las API Keys:**

- **Gemini AI:** https://aistudio.google.com/app/apikey (Gratis, 60 requests/min)
- **OpenWeatherMap:** https://openweathermap.org/api (Plan gratuito)

⚠️ **IMPORTANTE:** Nunca compartas tus API Keys ni las subas a GitHub. El archivo `.env` está en `.gitignore` para protegerlas.

4. **Verificar configuración:**
```bash
python config.py
```

Deberías ver:
```
✅ API Keys cargadas correctamente desde .env
✅ Modelo Gemini configurado: models/gemini-2.5-flash
✅ Cliente Gemini inicializado correctamente
```

5. **Probar el proyecto Weather API:**
```bash
cd 01-api-weather
python weather_app.py
```

---

## 🔒 Seguridad

Este repositorio implementa mejores prácticas de seguridad:

- ✅ API Keys almacenadas en `.env` (no versionado en Git)
- ✅ `.env.example` como plantilla pública
- ✅ Importación centralizada desde `config.py`
- ✅ Verificación de keys antes de ejecutar

**Nunca hardcodees API Keys en el código.**