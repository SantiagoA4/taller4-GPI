"""
Módulo con funciones utilitarias de estadística y transformación
"""
import pandas as pd
import numpy as np


def calcular_estadisticas(datos):
    """
    Calcula estadísticas descriptivas básicas
    
    Parameters:
    -----------
    datos : pd.DataFrame
        DataFrame con datos numéricos
    
    Returns:
    --------
    dict
        Diccionario con estadísticas
    """
    stats = {
        'media': datos.mean(),
        'mediana': datos.median(),
        'desvest': datos.std(),
        'minimo': datos.min(),
        'maximo': datos.max()
    }
    return stats


def agrupar_por_categoria(df, columna_agrupacion, columna_valor):
    """
    Agrupa datos y suma valores
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a agrupar
    columna_agrupacion : str
        Columna para agrupar
    columna_valor : str
        Columna con valores a sumar
    
    Returns:
    --------
    pd.Series
        Series con totales por grupo
    """
    return df.groupby(columna_agrupacion)[columna_valor].sum().sort_values(ascending=False)


def normalizar_datos(df, columnas):
    """
    Normaliza columnas al rango [0, 1]
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a normalizar
    columnas : list
        Lista de columnas a normalizar
    
    Returns:
    --------
    pd.DataFrame
        DataFrame con columnas normalizadas
    """
    df_norm = df.copy()
    for col in columnas:
        df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df_norm


def filtrar_por_rango(df, columna, minimo, maximo):
    """
    Filtra datos dentro de un rango
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a filtrar
    columna : str
        Columna a filtrar
    minimo : float
        Valor mínimo
    maximo : float
        Valor máximo
    
    Returns:
    --------
    pd.DataFrame
        DataFrame filtrado
    """
    return df[(df[columna] >= minimo) & (df[columna] <= maximo)]
