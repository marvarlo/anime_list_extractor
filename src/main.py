import logging
import os
import pandas as pd
from scraper import AnimeScraper
from dotenv import load_dotenv

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

def main():
    # Cargar variables de entorno desde el archivo .env si existe
    load_dotenv()

    logging.info("Iniciando el scraper de anime...")
    
    scraper = AnimeScraper()
    resultados = scraper.run()
    
    if resultados:
        # Guardar en data/
        os.makedirs("data", exist_ok=True)
        excel_path = "data/animes_perfil.xlsx"
        
        with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
            for category, animes in resultados.items():
                if animes:  # Solo crear pestaña si hay datos
                    df = pd.DataFrame(animes)
                    # Opcional: renombrar las columnas para que se vean mejor en Excel
                    df = df.rename(columns={"title": "Título", "link": "Link"})
                    # Limitar el nombre de la hoja a 31 caracteres (restricción de Excel)
                    sheet_name = category.replace("_", " ").title()[:31]
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
                    
        logging.info(f"Resultados guardados exitosamente en {excel_path}")
    else:
        logging.warning("No se obtuvieron resultados.")

if __name__ == "__main__":
    main()
