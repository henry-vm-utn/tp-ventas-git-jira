# TP Gestión Colaborativa con Git, GitHub y Jira

## Escenario elegido

Para este trabajo práctico elegí el Escenario B: análisis de ventas de una pequeña empresa.

El proyecto trabaja con un archivo de ventas simulado y realiza un análisis básico usando Python. A partir de esos datos se calculan indicadores simples, como ventas totales, producto más vendido y ventas por mes.

## Objetivo del proyecto

El objetivo principal es aplicar herramientas de organización y control de versiones en un proyecto sencillo de análisis de datos.

También se busca relacionar el trabajo técnico con la gestión del proyecto, usando Jira para organizar tareas, Git para registrar cambios y GitHub para guardar el repositorio.

## Organización del trabajo

Aunque el trabajo fue realizado de manera individual, se respetó la estructura de roles propuesta en la consigna:

- P1 - Líder y organizador: creación del repositorio, estructura inicial y documentación base.
- P2 - Desarrollador técnico: creación del dataset, script de análisis y generación de resultados.
- P3 - Revisor y QA: revisión de documentación, seguridad y Pull Request final.

## Estructura del repositorio

tp-ventas-git-jira/
- datos/
  - ventas.csv
- scripts/
  - analisis_ventas.py
- resultados/
  - ventas_por_mes.csv
  - resumen_ventas.txt
  - grafico_ventas_por_mes.png
- README.md
- revision_QA.md
- .gitignore

## Herramientas utilizadas

- Jira
- Git
- GitHub
- Google Colab
- Python

## Cómo ejecutar el proyecto

Desde la carpeta principal del repositorio, ejecutar:

python scripts/analisis_ventas.py

El script toma los datos desde:

datos/ventas.csv

y guarda los resultados en:

resultados/

## Resultados generados

El análisis genera:

- una tabla con las ventas agrupadas por mes;
- un resumen en texto con los principales indicadores;
- un gráfico simple de ventas por mes.

## Trazabilidad

Los commits se relacionan con las tareas creadas en Jira:

- TPV-1: configuración inicial del proyecto.
- TPV-2: desarrollo del análisis de ventas.
- TPV-3: revisión de documentación, seguridad y Pull Request.

De esta forma, cada parte del trabajo queda vinculada con una tarea del tablero.
