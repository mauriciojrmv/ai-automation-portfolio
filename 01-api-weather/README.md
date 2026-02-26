# 🌦️ Weather App - API Integration

Sistema de consulta de clima en tiempo real usando OpenWeatherMap API.

## 🎯 Características

- Consulta clima de cualquier ciudad del mundo
- Información detallada: temperatura, humedad, viento, condición
- Historial de consultas guardado en JSON
- Interfaz CLI amigable con emojis
- Manejo robusto de errores

## 🛠️ Tecnologías

- **Python 3.12**
- **requests** - HTTP requests
- **OpenWeatherMap API** - Datos meteorológicos

## 📦 Instalación

1. Clona este repositorio
2. Instala dependencias:
```bash
pip install requests
```

3. Obtén tu API Key gratuita en [OpenWeatherMap](https://openweathermap.org/api)

4. Edita `weather_app.py` y reemplaza `API_KEY` con tu key:
```python
API_KEY = "tu_api_key_aqui"
```

## 🚀 Uso
```bash
python weather_app.py
```

Ejemplo de salida:
```
╔══════════════════════════════════════╗
║   🌦️  WEATHER APP - CLIMA MUNDIAL   ║
╚══════════════════════════════════════╝

📍 Ingresa una ciudad: Santa Cruz

🔍 Buscando clima de Santa Cruz...

==================================================
🌤️  CLIMA EN SANTA CRUZ, BO
==================================================
🌡️  Temperatura: 28°C (Sensación: 30°C)
☁️  Condición: Cielo claro
💧 Humedad: 65%
💨 Viento: 2.5 m/s
==================================================

💾 Guardado en historial!
```

## 📊 Historial

Las consultas se guardan automáticamente en `weather_history.json`:
```json
[
  {
    "city": "Santa Cruz",
    "country": "BO",
    "temperature": 28.5,
    "condition": "cielo claro",
    "timestamp": "2026-02-26 14:30:00"
  }
]
```

## 🔧 Manejo de Errores

- ✅ Ciudad no encontrada
- ✅ Error de conexión a internet
- ✅ API Key inválida o no activa
- ✅ Rate limiting de API

## 📝 Próximas Mejoras

- [ ] Pronóstico de 5 días
- [ ] Gráficos de temperatura
- [ ] Alertas meteorológicas
- [ ] Comparación entre ciudades

## 👨‍💻 Autor

Mauricio Mattinen - [GitHub](https://github.com/mauriciojrmv)

## 📄 Licencia

MIT License