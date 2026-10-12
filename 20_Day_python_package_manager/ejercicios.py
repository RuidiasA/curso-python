import webbrowser  # módulo para abrir sitios web

# lista de URLs de ejemplo
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# abrir cada URL en una nueva pestaña
for url in url_lists:
    webbrowser.open_new_tab(url)
    
# Desinstalar paquetes --> Para eliminar un paquete instalado
# pip uninstall packagename


# Lista de paquetes --> Para listar los paquetes instalados en tu entorno
# pip list


# Mostrar información del paquete --> Para ver información de un paquete
# pip show packagename


# PIP Freeze --> Genera una lista de paquetes instalados y sus versiones (útil para requirements.txt)
# pip freeze


# Leer datos desde una URL --> A veces queremos leer datos desde una URL (por ejemplo APIs que devuelven JSON).
# pip install requests
# En requests veremos métodos y atributos como get(), status_code, headers, text, json():
#   get(): solicita una URL y devuelve un objeto Response
#   status_code: código HTTP de la respuesta
#   headers: cabeceras de la respuesta
#   text: contenido en texto
#   json(): parsea JSON y devuelve estructuras de Python


# Ejemplo leyendo un archivo de texto desde la web:
import requests # importar requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'  # URL con texto

response = requests.get(url)  # solicitar URL
print(response)
print(response.status_code)  # código de estado, 200 indica éxito
print(response.headers)      # cabeceras de la respuesta
print(response.text)         # contenido en texto


# Ejemplo leyendo una API que devuelve JSON (API de países):
url = 'https://restcountries.eu/rest/v2/all'  # API con información de países
response = requests.get(url)
print(response)                # objeto Response
print(response.status_code)    # 200 indica éxito
countries = response.json()
print(countries[:1])           # imprimimos el primer país por brevedad


# Veamos otro ejemplo con la API del Banco Mundial (datos de Etiopía):
from pprint import pp  # pretty print para mostrar resultados legibles

url = 'http://api.worldbank.org/countries/et?format=json'  # API del Banco Mundial para Etiopía
response = requests.get(url)
print(response)                # objeto Response
print(response.status_code)    # 200 indica éxito
ethiopia_data = response.json()
pp(ethiopia_data)              # mostrar datos de forma legible


# Usando paquete creado (mypackage)
from mypackage import arithmetics
print(arithmetics.add_numbers(1, 2, 3, 5))
print(arithmetics.subtract(5, 3))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(5, 3))
print(arithmetics.remainder(5, 3))
print(arithmetics.power(5, 3))

from mypackage import greet
print(greet.greet_person("Alejandro", "Ruidias"))


# Ejercicios: Día 20

# 1. Lee sobre entornos virtuales, crea uno e instala al menos un paquete dentro del entorno.

# 2. Usa una API de países para obtener todos los datos y encuentra los 10 países más poblados.
import requests

url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/json/countries.json"
response = requests.get(url)
countries = response.json()

top_pop_countries = []
"""
for country in countries:
    if "population" in country and country["population"] is not None:
        top_pop_countries.append({
            "Pais": country["name"],
            "Poblacion": country["population"] 
        })
    else:
        top_pop_countries.append({
            "Pais": country["name"],
            "Poblacion": 0
        })
"""
# Simplificado
for country in countries:
    top_pop_countries.append({
        "Pais": country.get("name"),
        "Poblacion": country.get("population") or 0
    })     


sorted_countries = sorted(top_pop_countries, key=lambda item: item["Poblacion"], reverse=True)
top_countries = sorted_countries[:10]

print(top_countries)

# 3. Encuentra todos los países cuyo idioma oficial sea inglés (código 'eng') a partir de los datos de la API.
import requests

url = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
response = requests.get(url)

countries = response.json()

top_eng_lang = []

for country in countries:
    if "eng" in country["languages"]:
        top_eng_lang.append({
            "Pais": country.get("name",{}).get("common")
        })

print(top_eng_lang)

# 4. A partir de los datos de la API, encuentra los 10 países con mayor superficie.
import requests

url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/json/countries.json"
response = requests.get(url)
countries = response.json()

top_area_countries = []

for country in countries:
    top_area_countries.append({
        "Pais": country.get("name"),
        "Area": country.get("area_sq_km") or 0
    })
    
sorted_countries = sorted(top_area_countries, key=lambda item: item["Area"], reverse=True)
top_ten_countries = sorted_countries[:10]
    
print(top_ten_countries)

# 5. Encuentra todos los países recién listados (o filtrados según la API) y ordénalos por capital.
import requests
url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/json/countries.json"
response = requests.get(url)
countries = response.json()

ord_cap = []

for country in countries:
    capital = country.get("capital")
    if capital: # --> Solo los que tienen una capital válida y no vacía
        ord_cap.append({
            "Pais": country.get("name"),
            "Capital": capital
        })

sorted_countries = sorted(ord_cap, key=lambda item: item["Capital"])
ord_asc = sorted_countries[:10] 

print(ord_asc)