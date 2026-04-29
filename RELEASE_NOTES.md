# Release Notes - Anime Scraper

## v1.0.0 (Release Inicial)

¡Bienvenido a la primera versión oficial del Anime Scraper!

### ✨ Características Principales
* **Autenticación con AnimeFLV:** El scraper ahora es capaz de iniciar sesión de forma segura y mantener la sesión HTTP activa.
* **Extracción de Perfil:**
  * Obtención automática de todos los animes en tu lista de **Siguiendo**.
  * Extracción de todos tus animes en la lista de **Favoritos**.
  * Extracción de la **Lista de espera**.
* **Exportación de Datos:** 
  * Los resultados ahora se guardan automáticamente en un archivo Excel (`animes_perfil.xlsx`).
  * Cada lista (Siguiendo, Favoritos, Lista de espera) se separa en su propia pestaña del archivo de Excel.
* **Seguridad y Configuración:** Uso de variables de entorno (con `.env` y `python-dotenv`) para no exponer credenciales directamente en el código fuente.

### 🛠 Mejoras Técnicas
* Arquitectura del código completamente modular (`main.py`, `config.py`, `scraper.py`, `http_client.py`, `anime_parser.py`).
* Dependencias limpias y manejadas mediante `requirements.txt`.
* Ignorado seguro de archivos sensibles mediante `.gitignore`.
