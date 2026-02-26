"""
Weather App - Consulta clima de cualquier ciudad
Usa OpenWeatherMap API
"""

import requests
import json
from datetime import datetime

# Tu API Key de OpenWeatherMap (REEMPLAZA con la tuya)
API_KEY = "9eea61dffa94f0749da50609329847bc"

# URL base de la API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """
    Obtiene información del clima de una ciudad
    
    Args:
        city_name (str): Nombre de la ciudad
    
    Returns:
        dict: Datos del clima o None si hay error
    """
    try:
        # Parámetros para la petición
        params = {
            'q': city_name,
            'appid': API_KEY,
            'units': 'metric',  # Celsius
            'lang': 'es'  # Respuestas en español
        }
        
        # Hacer la petición a la API
        print(f"\n🔍 Buscando clima de {city_name}...")
        response = requests.get(BASE_URL, params=params)
        
        # Verificar si la petición fue exitosa
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"❌ Ciudad '{city_name}' no encontrada.")
            return None
        else:
            print(f"❌ Error: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None

def display_weather(weather_data):
    """
    Muestra la información del clima de forma bonita
    
    Args:
        weather_data (dict): Datos del clima desde la API
    """
    if not weather_data:
        return
    
    # Extraer datos importantes
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']
    wind_speed = weather_data['wind']['speed']
    
    # Mostrar en pantalla
    print("\n" + "="*50)
    print(f"🌤️  CLIMA EN {city.upper()}, {country}")
    print("="*50)
    print(f"🌡️  Temperatura: {temp}°C (Sensación: {feels_like}°C)")
    print(f"☁️  Condición: {description.capitalize()}")
    print(f"💧 Humedad: {humidity}%")
    print(f"💨 Viento: {wind_speed} m/s")
    print("="*50)

def save_to_history(weather_data):
    """
    Guarda el resultado en un archivo JSON de historial
    
    Args:
        weather_data (dict): Datos del clima
    """
    if not weather_data:
        return
    
    # Agregar timestamp
    weather_data['consulted_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Leer historial existente
        try:
            with open('weather_history.json', 'r', encoding='utf-8') as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []
        
        # Agregar nueva consulta
        history.append({
            'city': weather_data['name'],
            'country': weather_data['sys']['country'],
            'temperature': weather_data['main']['temp'],
            'condition': weather_data['weather'][0]['description'],
            'timestamp': weather_data['consulted_at']
        })
        
        # Guardar historial actualizado
        with open('weather_history.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
        
        print("\n💾 Guardado en historial!")
        
    except Exception as e:
        print(f"⚠️  No se pudo guardar en historial: {e}")

def main():
    """
    Función principal del programa
    """
    print("╔══════════════════════════════════════╗")
    print("║   🌦️  WEATHER APP - CLIMA MUNDIAL   ║")
    print("╚══════════════════════════════════════╝")
    
    while True:
        # Pedir ciudad al usuario
        city = input("\n📍 Ingresa una ciudad (o 'salir' para terminar): ").strip()
        
        if city.lower() == 'salir':
            print("\n👋 ¡Hasta luego!")
            break
        
        if not city:
            print("❌ Por favor ingresa un nombre de ciudad.")
            continue
        
        # Obtener y mostrar clima
        weather_data = get_weather(city)
        display_weather(weather_data)
        
        # Guardar en historial
        if weather_data:
            save_to_history(weather_data)

if __name__ == "__main__":
    main()