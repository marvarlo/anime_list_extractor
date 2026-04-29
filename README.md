# Anime FLV List extractor

Proyecto en Python diseñado para hacer scraping de páginas de anime.

## Estructura del Proyecto

- `src/`: Contiene el código fuente del scraper.
  - `main.py`: Punto de entrada de la aplicación.
  - `config.py`: Variables de configuración (URLs, headers, etc.).
  - `scraper.py`: Lógica principal de orquestación del scraping.
  - `parsers/`: Módulos encargados de extraer la información de HTML/JSON.
  - `utils/`: Utilidades compartidas como clientes HTTP.
- `data/`: Directorio donde se guardarán los resultados del scraping (JSON, CSV).
- `requirements.txt`: Dependencias del proyecto.

## Instalación

1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

```bash
python src/main.py
```
