# Data Engineer Challenge — Olist Dataset

## Resumen
Este proyecto es un end-to-end pipeline de data engineering que utiliza el Olist Brazilian E-commerce dataset. Incluye data ingestion, limpieza, transformacion, modelado y visualizacion.

## Estructura
- data/: raw y processed datasets
- notebooks/: exploratory analysis
- scripts/: ingestion y transformation scripts
- sql/: database schema y queries
- dashboard/: visualizaciones

## Data Cleaning & Transformation
- Convertir timestamp a datetime
- Quitar duplicados en todas las tablas
- Quitar registros invalidos 
- Crear delivery_time_days para medir rendimiento logistico
- Crear total_order_value de datos de payments
- Extraido order_month para para analisis time-based