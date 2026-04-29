import requests
import logging
from config import HEADERS, LOGIN_URL, EMAIL, PASSWORD

class HttpClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.is_logged_in = False

    def login(self) -> bool:
        """Autenticarse en AnimeFLV."""
        payload = {
            "email": EMAIL,
            "password": PASSWORD,
            "remember_me": "1"
        }
        try:
            response = self.session.post(LOGIN_URL, data=payload)
            if response.status_code == 200:
                logging.info("Login exitoso en AnimeFLV.")
                self.is_logged_in = True
                return True
            else:
                logging.error("Error en login. Verifica tus credenciales.")
                return False
        except requests.exceptions.RequestException as e:
            logging.error(f"Error durante el login: {e}")
            return False

    def fetch_html(self, url: str) -> str:
        """Realiza una petición GET y devuelve el HTML."""
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                return response.text
            else:
                logging.warning(f"Error {response.status_code} al hacer GET a {url}")
                return ""
        except requests.exceptions.RequestException as e:
            logging.error(f"Error al hacer petición a {url}: {e}")
            return ""
