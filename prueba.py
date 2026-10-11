# Ejercicios: Nivel 3
# 1. Crea un archivo JSON a partir del siguiente dataset:
python_libraries = [
{
    "nombre_librería": "Django",
    "creador": "Adrian Holovaty",
    "primer_año_lanzamiento": 2005,
    "versión": "4.0.2",
    "uso": "Desarrollo web",
    "descripción": "Django permite construir aplicaciones web mejores y más rápido."
},
{
    "nombre_librería": "Flask",
    "creador": "Armin Ronacher",
    "primer_año_lanzamiento": 2010,
    "versión": "2.0.2",
    "uso": "Desarrollo web",
    "descripción": "Flask es un micro framework WSGI para aplicaciones web."
},
{
    "nombre_librería": "NumPy",
    "creador": "Travis Oliphant",
    "primer_año_lanzamiento": 2005,
    "versión": "1.22.0",
    "uso": "Cómputo científico",
    "descripción": "NumPy es la biblioteca fundamental para el cómputo científico en Python."
},
{
    "nombre_librería": "Pandas",
    "creador": "Wes McKinney",
    "primer_año_lanzamiento": 2008,
    "versión": "1.4.0",
    "uso": "Análisis de datos",
    "descripción": "pandas es una librería open source para análisis y manipulación de datos."
},
{
    "nombre_librería": "Matplotlib",
    "creador": "John D. Hunter",
    "primer_año_lanzamiento": 2003,
    "versión": "3.5.1",
    "uso": "Visualización de datos",
    "descripción": "Matplotlib es una librería para crear visualizaciones estáticas, animadas e interactivas en Python."
}
]

import json

with open("./files/python_libraries.json", "w", encoding="utf-8") as f:
    json.dump(python_libraries, f, ensure_ascii=False, indent=4)
    
print("Archivo JSON creado con éxito")