"""
Módulo para generar datos sintéticos
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generar_datos_ventas(n_registros=100, seed=42):
    """
    Genera datos sintéticos de ventas
    
    Parameters:
    -----------
    n_registros : int
        Número de registros a generar
    seed : int
        Semilla para reproducibilidad
    
    Returns:
    --------
    pd.DataFrame
        DataFrame con datos de ventas
    """
    np.random.seed(seed)
    
    # Fechas
    fecha_inicio = datetime(2024, 1, 1)
    fechas = [fecha_inicio + timedelta(days=int(x)) for x in np.random.randint(0, 365, n_registros)]
    
    # Datos
    datos = {
        'fecha': fechas,
        'producto': np.random.choice(['Producto A', 'Producto B', 'Producto C', 'Producto D'], n_registros),
        'cantidad': np.random.randint(1, 50, n_registros),
        'precio_unitario': np.random.uniform(10, 100, n_registros),
        'vendedor': np.random.choice(['Juan', 'María', 'Pedro', 'Ana'], n_registros),
        'región': np.random.choice(['Norte', 'Centro', 'Sur', 'Este'], n_registros)
    }
    
    df = pd.DataFrame(datos)
    df['venta_total'] = df['cantidad'] * df['precio_unitario']
    
    return df


if __name__ == "__main__":
    # Generar y guardar datos
    df = generar_datos_ventas(100)
    df.to_csv('data/raw/ventas_raw.csv', index=False)
    print(f"✓ Datos generados: {len(df)} registros")
    print(f"\nPrimeros registros:\n{df.head()}")
