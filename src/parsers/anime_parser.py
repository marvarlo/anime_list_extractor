from bs4 import BeautifulSoup
from config import BASE_URL

def parse_anime_list(html_content: str) -> list:
    """
    Parsea el HTML de AnimeFLV y extrae la lista de animes de una sección del perfil.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    animes = []
    
    ul = soup.find("ul", class_="ListAnimes AX Rows A06 C04 D03")
    if not ul:
        return animes

    for li in ul.find_all("li"):
        title_tag = li.find("h3", class_="Title")
        if title_tag and title_tag.a:
            title = title_tag.a.text.strip()
            link = BASE_URL + title_tag.a["href"]
            animes.append({"title": title, "link": link})
            
    return animes
