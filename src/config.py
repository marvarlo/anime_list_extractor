import os

# Configuración global del proyecto
BASE_URL = "https://www4.animeflv.net"

# Variables de entorno para login
EMAIL = os.getenv("ANIMEFLV_EMAIL", "tu_correo@example.com")
PASSWORD = os.getenv("ANIMEFLV_PASSWORD", "tu_contraseña")

# El nombre de usuario en la URL del perfil (se asume extraído del correo o configurado)
# Podemos pasarlo o extraerlo, para el ejemplo usaremos el username 'tu_username'
USERNAME = os.getenv("ANIMEFLV_USERNAME", "tu_username")

# URLs específicas de las secciones
LOGIN_URL = f"{BASE_URL}/auth/sign_in"
SECTIONS = {
    "siguiendo": f"{BASE_URL}/perfil/{USERNAME}/siguiendo",
    "favoritos": f"{BASE_URL}/perfil/{USERNAME}/favoritos",
    "lista_espera": f"{BASE_URL}/perfil/{USERNAME}/lista_espera"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

DELAY_BETWEEN_REQUESTS = 1  # segundos entre peticiones para ser amigables
