import requests
from bs4 import BeautifulSoup as bs

def scrap_info_hoteles(url):
    """
    Extrae información de los hoteles desde la página proporcionada.

    Parámetros:
    - url (str): URL de la página web donde se listan los hoteles.

    Retorna:
    - dict: Un diccionario con los siguientes datos:
        - "nombre_hotel": Lista de nombres de los hoteles.
        - "estrellas": Lista con la clasificación en estrellas de cada hotel.
        - "precio_noche": Lista con el precio por noche de cada hotel.

    Funcionalidad:
    - Realiza una solicitud HTTP a la URL dada.
    - Parsea el HTML con BeautifulSoup.
    - Encuentra los primeros 10 hoteles en la página (ajustable con `[:10]`).
    - Extrae el nombre, número de estrellas y precio por noche de cada hotel.
    - Devuelve un diccionario con la información recolectada.

    Requisitos:
    - Instalar `requests` y `beautifulsoup4` si no están disponibles:
      pip install requests beautifulsoup4
    """
    # Diccionario para almacenar los datos
    dictio_scrap = {
        "nombre_hotel": [],
        "estrellas": [],
        "precio_noche": []
    }

    # Realizar la solicitud HTTP
    res = requests.get(url)

    # Verificar si la respuesta fue exitosa
    if res.status_code == 200:
        sopa = bs(res.content, "html.parser")

        # Encontrar todos los hoteles en la página (máximo 10)
        hoteles = sopa.find_all("a", class_="title__link")[:10]

        for hotel in hoteles:
            # ✅ Nombre del hotel (solo el primer texto dentro del <a>)
            nombre_hotel = hotel.contents[0].strip() if hotel else "Sin nombre"

            # ✅ Estrellas del hotel
            estrellas = hotel.find("span", class_="sr-only")
            estrellas_hotel = estrellas.get_text(strip=True) if estrellas else "Sin estrellas"

            # ✅ Precio por noche
            precio = hotel.find("span", class_="booking-price__number mcp-price-number")
            precio_noche = precio.get_text(strip=True) if precio else "Sin precio"

            # Agregar cada dato en su lista correspondiente
            dictio_scrap["nombre_hotel"].append(nombre_hotel)
            dictio_scrap["estrellas"].append(estrellas_hotel)
            dictio_scrap["precio_noche"].append(precio_noche)

    return dictio_scrap