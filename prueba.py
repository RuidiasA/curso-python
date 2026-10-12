
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