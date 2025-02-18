def analisis_categoria(data_frame,columna):
    """
    Genera un análisis descriptivo de una columna categórica en un DataFrame.

    Parámetros:
    -----------
    data_frame : pandas.DataFrame
        El DataFrame que contiene los datos a analizar.
    columna : str
        El nombre de la columna categórica a analizar.

    Retorna:
    --------
    pandas.DataFrame
        Un DataFrame con las siguientes columnas:
        - 'index': Las categorías únicas de la columna analizada.
        - 'count': El conteo de ocurrencias de cada categoría.
        - 'porcentaje': El porcentaje que representa cada categoría
          respecto al total de datos en la columna.

    Notas:
    ------
    - El porcentaje se calcula con una precisión de dos decimales.
    - La salida está ordenada por las categorías con mayor frecuencia.

    Ejemplo:
    --------
    >>> data = {'col1': ['A', 'B', 'A', 'C', 'B', 'A']}
    >>> df = pd.DataFrame(data)
    >>> analisis_categoria(df, 'col1')
        index  count  porcentaje
    0      A      3       50.00
    1      B      2       33.33
    2      C      1       16.67
    """
    df_categoricas=pd.DataFrame(data_frame[columna].value_counts()).reset_index()
    df_categoricas["porcentaje"] =round(df_categoricas["count"]/df_categoricas["count"].sum()*100,2)
    return df_categoricas