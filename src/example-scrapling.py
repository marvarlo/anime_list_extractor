import requests
from bs4 import BeautifulSoup
import pandas as pd

# Datos de login (usa variables de entorno en producción, no hardcodees)
EMAIL = "youremail@mail.com"
PASSWORD = "yourpassword"
USERNAME = "yourusername"

# Crear sesión
session = requests.Session()

# Base URL
anime_url = "https://www4.animeflv.net"

# URL de login
login_url = f"{anime_url}/auth/sign_in"

# Payload del formulario
payload = {
    "email": EMAIL,
    "password": PASSWORD,
    "remember_me": "1"
}

# Enviar login
# Login
resp = session.post(login_url, data=payload)
if resp.status_code == 200:
    print("Login exitoso")
else:
    print("Error en login")

def scrape_section(base_url, max_pages=5):
    animes = []
    for page in range(1, max_pages+1):
        url = f"{base_url}?page={page}"
        r = session.get(url)
        if r.status_code != 200:
            break
        soup = BeautifulSoup(r.text, "html.parser")
        ul = soup.find("ul", class_="ListAnimes AX Rows A06 C04 D03")
        if not ul:
            break
        for li in ul.find_all("li"):
            title_tag = li.find("h3", class_="Title")
            if title_tag and title_tag.a:
                title = title_tag.a.text.strip()
                link = anime_url + title_tag.a["href"]
                animes.append({"Título": title, "Link": link})
    return animes

# Scrapear cada sección
siguiendo = scrape_section(f"{anime_url}/perfil/{USERNAME}/siguiendo", max_pages=10)
favoritos = scrape_section(f"{anime_url}/perfil/{USERNAME}/favoritos", max_pages=10)
espera    = scrape_section(f"{anime_url}/perfil/{USERNAME}/lista_espera", max_pages=10)

# Convertir a DataFrames
df_siguiendo = pd.DataFrame(siguiendo)
df_favoritos = pd.DataFrame(favoritos)
df_espera    = pd.DataFrame(espera)

# Guardar en Excel con 3 pestañas
with pd.ExcelWriter("animes.xlsx", engine="xlsxwriter") as writer:
    df_siguiendo.to_excel(writer, sheet_name="Siguiendo", index=False)
    df_favoritos.to_excel(writer, sheet_name="Favoritos", index=False)
    df_espera.to_excel(writer, sheet_name="Lista de espera", index=False)

print("Archivo Excel creado: animes.xlsx")