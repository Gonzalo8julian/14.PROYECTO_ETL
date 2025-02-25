from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_hoteles_accor(url, options):
    """
    Extrae información de hoteles desde la página de Accor usando Selenium.
    
    Parámetros:
    - url (str): URL de la página de hoteles de Accor.
    - options (webdriver.ChromeOptions): Opciones para el navegador Chrome.

    Retorna:
    - list[dict]: Lista de diccionarios con información de los hoteles.
    """
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Esperar a que la página cargue

    hoteles = driver.find_elements(By.CLASS_NAME, "hotelblock__content")
    hoteles_lista = []

    if not hoteles:
        print("No se encontraron hoteles")
    else:
        for hotel in hoteles:
            try:
                nombre = hotel.find_element(By.CLASS_NAME, "title__link").text.split("\n")[0].strip()
            except:
                nombre = "Sin nombre"

            try:
                estrellas = hotel.find_element(By.CLASS_NAME, "ratings__score").text.split("\n")[0].replace("/", "").strip()
            except:
                estrellas = "Sin estrellas"

            try:
                precio = hotel.find_element(By.CLASS_NAME, "booking-price").text.split("\n")[0].replace("€", "").strip()
                precio_noche = pd.to_numeric(precio, errors="coerce")
            except:
                precio_noche = "Sin precio"

            hoteles_lista.append({
                "nombre": nombre,
                "estrellas": estrellas,
                "precio_noche": precio_noche,
                "fecha_reserva": pd.to_datetime("2025-02-19", format="%Y-%m-%d")
            })

    driver.close()
    driver.quit()

    return hoteles_lista

#API

import pandas as pd
import numpy as np
import requests

def obtener_eventos_madrid(url, inicio_estancia, final_estancia):
    """
    Obtiene eventos de Madrid desde la API de datos abiertos y los filtra por un rango de fechas.

    Parámetros:
    - url (str): URL de la API de eventos de Madrid.
    - inicio_estancia (str): Fecha de inicio de la estancia en formato "YYYY-MM-DD".
    - final_estancia (str): Fecha de fin de la estancia en formato "YYYY-MM-DD".

    Retorna:
    - dict: Diccionario con la información de los eventos filtrados.
    """
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Error al obtener los datos")
        return {}

    data = response.json()

    info_eventos = {
        "nombre_evento": [],
        "url_evento": [],
        "codigo_postal": [],
        "direccion": [],
        "horario": [],
        "organizacion": [],
        "fecha_inicio": [],
        "fecha_fin": [],
        "ciudad": []
    }

    inicio_estancia = pd.to_datetime(inicio_estancia)
    final_estancia = pd.to_datetime(final_estancia)

    for evento in data.get("@graph", []):
        try:
            start_date = pd.to_datetime(evento.get('dtstart'))
            end_date = pd.to_datetime(evento.get('dtend'))
        except:
            continue  # Si no puede convertir las fechas, salta el evento

        if start_date <= final_estancia and end_date >= inicio_estancia:
            info_eventos["nombre_evento"].append(evento.get('title'))
            info_eventos["url_evento"].append(evento.get('link'))
            address = evento.get("address", {})
            area = address.get("area", {}) 
            info_eventos["codigo_postal"].append(area.get("postal-code", np.nan))
            info_eventos["direccion"].append(area.get("street-address", np.nan))
            info_eventos["horario"].append(evento.get("time"))
            organizacion = evento.get('organization', {})
            info_eventos["organizacion"].append(organizacion.get('organization-name', np.nan))
            info_eventos["fecha_inicio"].append(start_date.strftime("%Y-%m-%d"))
            info_eventos["fecha_fin"].append(end_date.strftime("%Y-%m-%d"))
            info_eventos["ciudad"].append(area.get("locality", np.nan).capitalize() if area.get("locality") else np.nan)

    return info_eventos