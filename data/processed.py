"""
Módulo de procesamiento de datos
"""
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.estadisticas import calcular_estadisticas, normalizar_datos


def limpiar_datos(df):
    """
    Limpia datos: elimina duplicados y valores nulos
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a limpiar
    
    Returns:
    --------
    pd.DataFrame
        DataFrame limpio
    """
    df_limpio = df.drop_duplicates()
    df_limpio = df_limpio.dropna()
    return df_limpio


def enriquecimiento_datos(df):
    """
    Agrega nuevas características a los datos
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame original
    
    Returns:
    --------
    pd.DataFrame
        DataFrame con nuevas características
    """
    df_enriquecido = df.copy()
    
    # Extraer fecha
    if 'fecha' in df.columns:
        df_enriquecido['fecha'] = pd.to_datetime(df_enriquecido['fecha'])
        df_enriquecido['mes'] = df_enriquecido['fecha'].dt.month
        df_enriquecido['año'] = df_enriquecido['fecha'].dt.year
        df_enriquecido['dia_semana'] = df_enriquecido['fecha'].dt.day_name()
    
    # Categorizar venta_total si existe
    if 'venta_total' in df.columns:
        df_enriquecido['categoria_venta'] = pd.cut(
            df_enriquecido['venta_total'],
            bins=[0, 500, 1500, np.inf],
            labels=['Baja', 'Media', 'Alta']
        )
    
    return df_enriquecido


if __name__ == "__main__":
    # Cargar datos
    df = pd.read_csv('data/raw/ventas_raw.csv')
    
    print("Datos originales:", len(df), "registros")
    print(df.head())
    
    # Procesar
    df_limpio = limpiar_datos(df)
    df_enriquecido = enriquecimiento_datos(df_limpio)
    
    # Guardar
    df_enriquecido.to_csv('data/processed/ventas_procesadas.csv', index=False)
    
    print(f"\n✓ Datos procesados: {len(df_enriquecido)} registros")
    print(f"\nÚltimos registros:\n{df_enriquecido.tail()}")
