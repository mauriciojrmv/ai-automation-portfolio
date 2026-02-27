"""
Test de seguridad - Verifica que no hay API Keys expuestas
"""

import os
from pathlib import Path

def check_files_for_keys(directory):
    """Busca API keys hardcodeadas en archivos Python"""
    
    issues = []
    
    # Patrones sospechosos
    patterns = [
        'AIzaSy',  # Gemini API keys empiezan con esto
        'api_key = "',
        'API_KEY = "',
        'apikey="',
    ]
    
    # Buscar en todos los .py excepto este archivo
    for py_file in Path(directory).rglob('*.py'):
        if py_file.name == 'test_security.py':
            continue
            
        try:
            content = py_file.read_text(encoding='utf-8')
            
            for pattern in patterns:
                if pattern in content and 'your_' not in content.lower():
                    issues.append(f"⚠️  Posible API key en: {py_file}")
                    
        except Exception as e:
            pass
    
    return issues

def check_env_files():
    """Verifica que .env no está en Git"""
    
    issues = []
    
    # Verificar que .env existe
    if not Path('.env').exists():
        issues.append("❌ .env no existe - créalo con tus API keys")
    
    # Verificar que .env.example existe
    if not Path('.env.example').exists():
        issues.append("⚠️  .env.example no existe - créalo como plantilla")
    
    # Verificar que .gitignore tiene .env
    if Path('.gitignore').exists():
        gitignore = Path('.gitignore').read_text()
        if '.env' not in gitignore:
            issues.append("❌ .gitignore no ignora .env - agrégalo")
    
    return issues

def main():
    print("🔒 Test de Seguridad de API Keys")
    print("=" * 60)
    
    # Check 1: Archivos con keys
    print("\n1. Buscando API keys hardcodeadas en código...")
    issues = check_files_for_keys('.')
    
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("✅ No se encontraron API keys hardcodeadas")
    
    # Check 2: Archivos .env
    print("\n2. Verificando configuración de .env...")
    env_issues = check_env_files()
    
    if env_issues:
        for issue in env_issues:
            print(issue)
    else:
        print("✅ Configuración de .env correcta")
    
    # Check 3: Config.py
    print("\n3. Verificando config.py...")
    try:
        from config import verify_keys
        verify_keys()
    except Exception as e:
        print(f"❌ Error en config.py: {e}")
    
    print("\n" + "=" * 60)
    
    if not issues and not env_issues:
        print("✅ ¡TODO SEGURO! No hay API keys expuestas.")
    else:
        print("⚠️  Revisa los problemas anteriores antes de hacer commit")

if __name__ == "__main__":
    main()