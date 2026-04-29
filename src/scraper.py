import time
import logging
from utils.http_client import HttpClient
from parsers.anime_parser import parse_anime_list
from config import SECTIONS, DELAY_BETWEEN_REQUESTS

class AnimeScraper:
    def __init__(self):
        self.client = HttpClient()

    def run(self):
        """Orquesta el scraping de las distintas secciones del perfil."""
        # 1. Hacer Login
        if not self.client.login():
            logging.error("No se puede continuar sin iniciar sesión.")
            return {}

        resultados = {}

        # 2. Scrapear cada sección (siguiendo, favoritos, lista de espera)
        for section_name, base_url in SECTIONS.items():
            logging.info(f"Iniciando scraping de la sección: {section_name}")
            section_animes = self._scrape_section(base_url, max_pages=10)
            resultados[section_name] = section_animes
            logging.info(f"Se encontraron {len(section_animes)} animes en {section_name}.")

        return resultados

    def _scrape_section(self, base_url: str, max_pages: int) -> list:
        """Scrapea todas las páginas de una sección específica."""
        animes = []
        for page in range(1, max_pages + 1):
            url = f"{base_url}?page={page}"
            logging.debug(f"Petición a: {url}")
            
            html_content = self.client.fetch_html(url)
            if not html_content:
                break # Si no hay html, paramos

            page_animes = parse_anime_list(html_content)
            if not page_animes:
                # Si la página no contiene animes, asumimos que llegamos al final
                break
                
            animes.extend(page_animes)
            
            # Respetamos el servidor
            time.sleep(DELAY_BETWEEN_REQUESTS)
            
        return animes
