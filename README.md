# Data Engineer Challenge — Olist Dataset

## Resumen
Este proyecto es un end-to-end pipeline de data engineering que utiliza el Olist Brazilian E-commerce dataset. Incluye data ingestion, limpieza, transformacion, modelado y visualizacion.

## Estructura
- data/: raw y processed datasets
- notebooks/: exploratory analysis
- scripts/: ingestion y transformation scripts
- sql/: database schema y queries
- dashboard/: visualizaciones

## Fase 2: Data Cleaning & Transformation
- Convertir timestamp a datetime
- Quitar duplicados en todas las tablas
- Quitar registros invalidos 
- Crear delivery_time_days para medir rendimiento logistico
- Crear total_order_value de datos de payments
- Extraido order_month para para analisis time-based

## Fase 3: Modelado y Carga en Base de Datos

El dataset Olist limpio de modelo en un schema relacional analitico usando SQLite.

### Diseno de schema
- fact_orders es la tabla central para metricas a nivel de pedido
- dim_customers y dim_products son dimensiones descriptivas
- fact_order_items, fact_payments y fact_reviews apoyan analisis de valores, pagos e incidentes.
- dim_sellers para mantener el contexto de sellers

### Justificacion
Este diseño se utilizo por las siguientes razones:
- Apoya analisis de volumen de transacciones de tipo series de tiempo
- Se puede indentificar clientes/productos/categorias top por su valor generado
- Calculo de promedio de delivery times
- Cuantificar incidentes como cancelaciones y reseñas malas

### Proceso de carga
Se cargan los CSVs limpios de data/processed a SQLite a traves de scripts/load.py
1. Crear el schema con sql/create_tables.sql
2. Inserta todos los registros a la base de datos
3. Valida la carga haciendo print de los row counts

## Fase 4: Visualización y Dashboard

## Insights Clave

- **Q1 — Volumen de Transacciones Mensual:**  
El volumen de órdenes muestra un crecimiento sostenido a lo largo del tiempo, con un pico hacia finales de 2017, probablemente impulsado por eventos estacionales como promociones de fin de año.

- **Q2 — Generadores de Valor:**  
Los ingresos están concentrados en un número reducido de categorías, lideradas por *beleza_saude* y *relogios_presentes*, lo que sugiere una distribución tipo Pareto.

- **Q3 — Tiempo de Entrega:**  
El tiempo promedio de entrega es aproximadamente X días, con la mayoría de entregas en rangos bajos, pero con algunos casos extremos que afectan el promedio.

- **Q4 — Resultados Negativos:**  
Aproximadamente X% de las órdenes presentan resultados negativos (cancelaciones o bajas calificaciones), lo que indica un buen desempeño general con oportunidades de mejora.

- **Q5 — Entrega vs Satisfacción:**  
Los pedidos con retrasos presentan menores calificaciones, evidenciando una relación directa entre el desempeño logístico y la satisfacción del cliente.