"""
Script de análisis de datos
"""
import pandas as pd
import sys
sys.path.append('.')

from src.estadisticas import calcular_estadisticas, agrupar_por_categoria


def analizar_ventas():
    """Análisis principal de los datos de ventas"""
    
    # Cargar datos procesados
    df = pd.read_csv('data/processed/ventas_procesadas.csv')
    
    print("=" * 60)
    print("ANÁLISIS DE VENTAS")
    print("=" * 60)
    
    # Estadísticas generales
    print("\n1. ESTADÍSTICAS DE VENTA TOTAL")
    print("-" * 40)
    stats = calcular_estadisticas(df[['venta_total']])
    for metrica, valor in stats.items():
        print(f"{metrica.capitalize():15s}: ${valor['venta_total']:,.2f}")
    
    # Ventas por producto
    print("\n2. VENTAS POR PRODUCTO")
    print("-" * 40)
    ventas_producto = agrupar_por_categoria(df, 'producto', 'venta_total')
    for producto, total in ventas_producto.items():
        print(f"{producto:15s}: ${total:,.2f}")
    
    # Ventas por región
    print("\n3. VENTAS POR REGIÓN")
    print("-" * 40)
    ventas_region = agrupar_por_categoria(df, 'región', 'venta_total')
    for region, total in ventas_region.items():
        print(f"{region:15s}: ${total:,.2f}")
    
    # Ventas por vendedor
    print("\n4. VENTAS POR VENDEDOR")
    print("-" * 40)
    ventas_vendedor = agrupar_por_categoria(df, 'vendedor', 'venta_total')
    for vendedor, total in ventas_vendedor.items():
        print(f"{vendedor:15s}: ${total:,.2f}")
    
    # Resumen general
    print("\n5. RESUMEN GENERAL")
    print("-" * 40)
    print(f"Total de registros    : {len(df)}")
    print(f"Venta total           : ${df['venta_total'].sum():,.2f}")
    print(f"Venta promedio        : ${df['venta_total'].mean():,.2f}")
    print(f"Cantidad total vendida: {df['cantidad'].sum()}")
    print("=" * 60)


if __name__ == "__main__":
    analizar_ventas()
