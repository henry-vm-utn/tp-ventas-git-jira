# TP Gestión Colaborativa con Git, GitHub y Jira

## Escenario elegido

Para este trabajo práctico elegí el Escenario B: análisis de ventas de una pequeña empresa.

La idea del proyecto es trabajar con un archivo de ventas simulado y realizar un análisis básico usando Python. A partir de esos datos se van a calcular algunos indicadores simples, como las ventas totales, el producto más vendido y la evolución de las ventas por mes.

## Objetivo del proyecto

El objetivo principal es aplicar herramientas de organización y control de versiones en un proyecto sencillo de análisis de datos.

Además del código, el trabajo busca mostrar cómo se puede organizar un proyecto usando Jira para dividir tareas, Git para registrar cambios y GitHub para guardar el repositorio de forma remota.

## Organización del trabajo

Aunque el trabajo fue realizado de manera individual, se respetó la estructura de roles propuesta en la consigna, simulando una pequeña célula de desarrollo:

- P1 - Líder y organizador: encargado de crear el repositorio, preparar la estructura de carpetas y dejar una primera documentación del proyecto.
- P2 - Desarrollador técnico: encargado de crear los datos de ventas, desarrollar el script de análisis y generar los resultados.
- P3 - Revisor y QA: encargado de revisar la documentación, controlar que no se suban archivos innecesarios o sensibles y preparar la integración final.

## Estructura del repositorio

El repositorio se organiza de la siguiente manera:

tp-ventas-git-jira/
- datos/
- scripts/
- resultados/
- README.md
- .gitignore

La carpeta `datos` se usa para guardar el archivo CSV con la información de ventas.

La carpeta `scripts` contiene el archivo de Python que realiza el análisis.

La carpeta `resultados` se utiliza para guardar los archivos generados por el script, como tablas, resúmenes o gráficos.

## Herramientas utilizadas

Para realizar el trabajo se utilizan las siguientes herramientas:

- Jira, para organizar las tareas del proyecto.
- Git, para llevar el control de versiones.
- GitHub, para almacenar el repositorio en la nube.
- Google Colab, para trabajar con Git y ejecutar el código.
- Python, para procesar los datos y generar resultados.

## Trazabilidad

Para relacionar la planificación del trabajo con los cambios realizados en el repositorio, los commits se identifican con el código de cada tarea creada en Jira:

- TPV-1: configuración inicial del proyecto.
- TPV-2: desarrollo del análisis de ventas.
- TPV-3: revisión de documentación, seguridad y Pull Request.

De esta manera, cada cambio importante queda asociado a una tarea concreta del tablero de Jira.
