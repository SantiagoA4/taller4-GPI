"""
Script para generar visualizaciones
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
sys.path.append('.')

from src.estadisticas import agrupar_por_categoria

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)


def generar_visualizaciones():
    """Genera gráficos de los datos"""
    
    # Cargar datos
    df = pd.read_csv('data/processed/ventas_procesadas.csv')
    
    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Análisis de Ventas', fontsize=16, fontweight='bold')
    
    # Gráfico 1: Ventas por producto
    ventas_producto = agrupar_por_categoria(df, 'producto', 'venta_total')
    axes[0, 0].bar(ventas_producto.index, ventas_producto.values, color='steelblue')
    axes[0, 0].set_title('Ventas por Producto')
    axes[0, 0].set_ylabel('Venta Total ($)')
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Gráfico 2: Ventas por región
    ventas_region = agrupar_por_categoria(df, 'región', 'venta_total')
    axes[0, 1].bar(ventas_region.index, ventas_region.values, color='coral')
    axes[0, 1].set_title('Ventas por Región')
    axes[0, 1].set_ylabel('Venta Total ($)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Gráfico 3: Ventas por vendedor
    ventas_vendedor = agrupar_por_categoria(df, 'vendedor', 'venta_total')
    axes[1, 0].barh(ventas_vendedor.index, ventas_vendedor.values, color='mediumseagreen')
    axes[1, 0].set_title('Ventas por Vendedor')
    axes[1, 0].set_xlabel('Venta Total ($)')
    
    # Gráfico 4: Distribución de cantidad vendida
    axes[1, 1].hist(df['cantidad'], bins=20, color='gold', edgecolor='black', alpha=0.7)
    axes[1, 1].set_title('Distribución de Cantidad Vendida')
    axes[1, 1].set_xlabel('Cantidad')
    axes[1, 1].set_ylabel('Frecuencia')
    
    plt.tight_layout()
    plt.savefig('results/figures/analisis_ventas.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: results/figures/analisis_ventas.png")
    plt.close()


if __name__ == "__main__":
    generar_visualizaciones()
