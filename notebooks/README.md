# Project Builder

## ¿Qué es?
**Project Builder** es un sistema de recomendación de herramientas diseñado para desarrolladores o cualquier persona interesada en llevar a cabo una idea relacionada con un proyecto tecnológico.

## Tecnologías utilizadas
- **Visual Studio Code**
- **Python**
- **Ficheros CSV**
- **Jupyter Notebook**
- **API de OpenAI**
- **StreamLit**

## Formato
Project Builder cuenta con una interfaz web muy sencilla para facilitar su uso.

## Diagrama de Arquitectura
Incluye una representación visual del sistema mediante un diagrama de arquitectura.

![Diagrama de Arquitectura](img/ArchitectureDiagram.png)

## Ideas de Mejora
- Crear botón para exportar a CSV/Excel.
- Añadir un sistema de puntuación/valoración a cada herramienta.

## Manual de uso
1. El usuario introduce su idea en un campo de texto.
2. Se rellenan todos los posibles sectores de proyectos que pueden ser utilizados:
   - **Front-end**
   - **Back-end**
   - **Database**
   - **Authentication**
   - **Ecommerce**
   - **Message system**
3. Cada sector cuenta con sus subparámetros correspondientes.

## Estructura del Proyecto
La organización de carpetas sigue la siguiente estructura:

```
Project-Builder/
│-- data/
│   │-- jupyter_checkpoints/
│   │-- auth-pro.csv
│   │-- auth-prueba.csv
│   │-- auth.csv
│   │-- back-end.csv
│   │-- database.csv
│   │-- ecommerce.csv
│   │-- front-end.csv
│   │-- message.csv
│   │-- recommender_dataset.csv
│   │-- search_engine.csv
│   └-- Tabla_Prinal.xlsx
│
│-- front/
│   └-- front-end.py
│
│-- img/
│   │-- ArchitectureDiagram.png
│   │-- backlog-workflow.png
│   │-- PreDiagram.png
│   └-- ProjectBuilderLogo.jpeg
│
My-info/
│-- .ipynb_checkpoints/
│-- info.txt
│-- prueba.json
│-- Respuesta_Completa.txt
│-- Untitled.ipynb
│-- notebooks/
│   │-- .ipynb_checkpoints/
│-- prompts/
│   │-- APIOpenAI.ipynb
│   │-- create_ecommerce_dataset.ipynb
│   │-- List-Datasets.ipynb
│   │-- Modelo-Local.ipynb
│
└-- README.md
```