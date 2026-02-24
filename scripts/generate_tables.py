"""
Módulo para generar tablas de resumen
"""
import pandas as pd
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.estadisticas import agrupar_por_categoria


def generar_tablas_resumen():
    """Genera tablas de resumen y las guarda"""
    
    # Cargar datos
    df = pd.read_csv('data/processed/ventas_procesadas.csv')
    
    # Tabla 1: Resumen por producto
    resumen_producto = df.groupby('producto').agg({
        'venta_total': ['sum', 'mean', 'count'],
        'cantidad': 'sum'
    }).round(2)
    resumen_producto.columns = ['Venta Total', 'Venta Promedio', 'Cantidad Registros', 'Cantidad Vendida']
    resumen_producto.to_csv('results/tables/resumen_producto.csv')
    
    # Tabla 2: Resumen por región
    resumen_region = df.groupby('región').agg({
        'venta_total': ['sum', 'mean', 'count']
    }).round(2)
    resumen_region.columns = ['Venta Total', 'Venta Promedio', 'Cantidad Registros']
    resumen_region.to_csv('results/tables/resumen_region.csv')
    
    # Tabla 3: Resumen por vendedor
    resumen_vendedor = df.groupby('vendedor').agg({
        'venta_total': ['sum', 'mean', 'count'],
        'cantidad': 'sum'
    }).round(2)
    resumen_vendedor.columns = ['Venta Total', 'Venta Promedio', 'Cantidad Registros', 'Cantidad Vendida']
    resumen_vendedor.to_csv('results/tables/resumen_vendedor.csv')
    
    print("✓ Tablas generadas:")
    print("  - results/tables/resumen_producto.csv")
    print("  - results/tables/resumen_region.csv")
    print("  - results/tables/resumen_vendedor.csv")


if __name__ == "__main__":
    generar_tablas_resumen()
