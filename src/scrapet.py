import requests
from bs4 import BeautifulSoup as bs

def scrap_info_hoteles(url):
    """
    Extrae información de hoteles desde una página web mediante web scraping.
    
    Parámetros:
    - url (str): URL de la página web donde se encuentran los hoteles.

    Retorna:
    - dict: Un diccionario con la información extraída, con las claves:
        - "nombre_hotel": Lista de nombres de los hoteles.
        - "descripcion": Lista de descripciones de los hoteles.
        - "valoracion": Lista de valoraciones de los hoteles en formato float.
    
    Ejemplo de uso:
    ```python
    url_hoteles = "https://ibis.accor.com/es/destination/city/hotels-madrid-v2418.html"
    datos_hoteles = scrap_info_hoteles(url_hoteles)
    ```
    """
    dictio_scrap = {
        "nombre_hotel": [],
        "descripcion": [],
        "valoracion": []
    }

    res_hoteles = requests.get(url)

    if res_hoteles.status_code == 200:
        sopa_hoteles = bs(res_hoteles.content, "html.parser")

        # Buscar los hoteles y manejar caso en que la lista esté vacía
        hoteles = sopa_hoteles.find_all("li", class_="aem-GridColumn aem-GridColumn--default--3")
        hoteles = hoteles[:9] if hoteles else []  # Evita errores de slicing si está vacío

        for hotel in hoteles:
            # Extraer nombre del hotel
            nombre = hotel.find("h3")
            nombre_hotel = nombre.get_text(strip=True) if nombre else "Sin nombre"

            # Extraer descripción
            descripcion = hotel.find("p")
            descripcion_texto = descripcion.get_text(strip=True) if descripcion else "Sin descripción"

            # Extraer valoración
            valoracion = hotel.find("span", class_="cmp-teaser__rating-score")
            valoracion_texto = valoracion.get_text(strip=True) if valoracion else "Sin valoración"

            # Limpiar y convertir la valoración a float
            if valoracion_texto != "Sin valoración":
                valoracion_texto = valoracion_texto.split("/")[0]  # Tomar solo el número antes de "/"
                valoracion_texto = valoracion_texto.replace(",", ".")  # Convertir "4,7" a "4.7"
                try:
                    valoracion_texto = float(valoracion_texto)
                except ValueError:
                    valoracion_texto = "Error en conversión"

            # Agregar datos al diccionario
            dictio_scrap["nombre_hotel"].append(nombre_hotel)
            dictio_scrap["descripcion"].append(descripcion_texto)
            dictio_scrap["valoracion"].append(valoracion_texto)

    return dictio_scrap
