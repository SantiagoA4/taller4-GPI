# Script para ejecutar simulación, análisis y visualización
# Ejecutar con: .\runall.ps1

Write-Host "=== Iniciando pipeline de GPI ===" -ForegroundColor Green

# 1. Generar datos simulados
Write-Host "`nPaso 1: Generando datos simulados..." -ForegroundColor Cyan
python data/raw.py

# 2. Procesar datos
Write-Host "`nPaso 2: Procesando datos..." -ForegroundColor Cyan
python data/processed.py

# 3. Ejecutar análisis
Write-Host "`nPaso 3: Ejecutando análisis..." -ForegroundColor Cyan
# Agregar scripts de análisis aquí
# python scripts/analysis.py

# 4. Generar visualizaciones
Write-Host "`nPaso 4: Generando visualizaciones..." -ForegroundColor Cyan
# Agregar scripts de visualización aquí
# python scripts/visualization.py

Write-Host "`n=== Pipeline completado ===" -ForegroundColor Green
