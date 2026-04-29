# Anime FLV List extractor

Proyecto en Python diseñado para hacer scraping de páginas de anime.

## Estructura del Proyecto

- `src/`: Contiene el código fuente del scraper.
  - `main.py`: Punto de entrada de la aplicación.
  - `config.py`: Variables de configuración (URLs, headers, etc.).
  - `scraper.py`: Lógica principal de orquestación del scraping.
  - `parsers/`: Módulos encargados de extraer la información de HTML/JSON.
  - `utils/`: Utilidades compartidas como clientes HTTP.
- `data/`: Directorio donde se guardan los resultados del scraping (archivo Excel `.xlsx` con pestañas por categoría).
- `requirements.txt`: Dependencias del proyecto (incluye `pandas` y `xlsxwriter`).
- `.env.example`: Plantilla para configurar tus credenciales de AnimeFLV.

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
3. Configura tus credenciales:
   - Copia el archivo `.env.example` y renómbralo a `.env`.
   - Modifica el archivo `.env` para colocar tu usuario, correo y contraseña de AnimeFLV.

## Ejecución

```bash
python src/main.py
```

Una vez que termine la ejecución, el script generará automáticamente un archivo **Excel** en la ruta `data/animes_perfil.xlsx`. Este documento contendrá una pestaña independiente por cada sección de tu perfil (Siguiendo, Favoritos, Lista de espera, etc.).
