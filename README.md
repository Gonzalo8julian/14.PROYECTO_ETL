# 📊 PROYECTO_ETL

## 📚 Descripción
Este proyecto realiza un proceso de Extracción, Transformación y Carga de datos en una base de datos SQL para poder analizar el rendimiento de una cadena de hoteles de Madrid. El objetivo es poder analizar una primera base de datos dada, extraer mediante web scrapping información adicional de la competencia, extraer datos de una API y cargar todo en una base de datos SQL para poder realizar un análisis exhaustivo de la situación de la compañía.

Los procesos llevados a cabo han sido los siguientes: 

1. **Análisis y limpieza de los datos dados**: Se nos facilita un archivo parquet con datos de hoteles propios y de la competencia. Se han limpiado los datos y se han eliminado las columnas que no aportaban información relevante para el análisis.

2. **Web Scrapping**: Se ha realizado un web scrapping de la página web de all.accor para obtener información de los hoteles de la competencia. Se han extraído datos como el nombre del hotel, el precio por noche y la valoración de cada uno de ellos.

3. **API**: Se ha extraido información de la API del Ayuntamiento de Madrid para obtener información de los eventos que se realizan en la ciudad durante las fechas de las reservas a analizar.

4. **Carga de datos**: Se han cargado todos los datos en una base de datos SQL para poder realizar un análisis exhaustivo de la situación de la compañía. Las tablas creadas han sido las siguientes:

    - **Ciudad**: Tabla con los datos de la ciudad y su id.
    - **Eventos**: Tabla con la información de los eventos de Madrid durante las fechas establecidas.
    - **Hoteles**: Tabla con los datos de los hoteles únicos propios y de la competencia.
    - **Clientes**: Tabla con los datos de los clientes que han realizado reservas.
    - **Reservas**: Tabla con los datos de las reservas realizadas por los clientes.

## 🗂️ Estructura del Proyecto

```
├── Data/                      # Archivos parquet y csv con los datos de hoteles, competencia y eventos.
├── Notebooks/                 # Notebooks con el análisis y limpieza de datos
├── Web_Scrapping/             # Archivos con el código de web scrapping
├── API/                       # Archivos con el código de la API
├── SQL/                       # Archivos con el código SQL para la creación de tablas
├── README.md                  # Descripción del proyecto
``` 

## 🛠️ Instalación y Requisitos
Este proyecto usa Python 3.8 y requiere las siguientes bibliotecas:

```Pandas
Numpy
Requests
BeautifulSoup
SQLAlchemy 
Selenium
```

## 📊 Resultados y Conclusiones
- Limpieza de datos: Hemos limpiado los datos del archivo parquet proporcionado para poder cargar los datos a la base de datos SQL.

- Web Scrapping: Hemos extraído información de la página web de all.accor para obtener información de los hoteles de la competencia.

- API: Hemos extraído información de la API del Ayuntamiento de Madrid para obtener información de los eventos que se realizan en la ciudad durante las fechas de las reservas a analizar.

- Carga: Carga de todos los datos en una base de datos SQL para poder realizar un análisis exhaustivo de la situación de la compañía.

## 🔄 Próximos Pasos
- Realizar un análisis de los datos cargados en la base de datos SQL para poder sacar conclusiones y tomar decisiones de cara al futuro de la compañía.
- Realizar un análisis de la competencia para poder comparar los datos de los hoteles propios con los de la competencia.
- Realizar un análisis de los eventos de Madrid para poder ver si influyen en las reservas de los hotel.

## ✒️ Autor
- **Gonzalo Julián** - [@gonzalo8julian](https://github.com/Gonzalo8julian)







