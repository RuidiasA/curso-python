# Ejercicios: Nivel 1

# 1. Declara una lista vacía
list_1 = []
list_2 = list()

# 2. Declara una lista con más de 5 elementos
list_3 = [1, "uno", 2, "dos", 3, "tres", 4, "cuatro", 5, "cinco"]

# 3. Encuentra la longitud de la lista
print(len(list_3))

# 4. Obtén el primer, medio y último elemento de la lista
mid_item = len(list_3) // 2
print(
    f"Primer elemento: {list_3[0]}\nElemento del medio: {list_3[mid_item]}\nUltimo elemento: {list_3[-1]}")

# 5. Declara una lista llamada mixed_data_types que contenga tu nombre, edad, altura, estado civil y dirección
mixed_data_types = ["Alejandro", 23, 1.70, "Soltero", "Lima, Peru"]

# 6. Declara una lista it_companies e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
it_companies = ["Facebook", "Google", "Microsoft",
                "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprime la lista usando print()
print(it_companies)

# 8. Imprime el número de empresas en la lista
print(len(it_companies))

# 9. Imprime la primera, la del medio y la última empresa
first_item, *rest, last_item = it_companies
print(f"Primera: {first_item}\nMedio: {it_companies[-4]}\nUltima: {last_item}")

# 10. Cambia el nombre de una de las empresas y vuelve a imprimir la lista
it_companies[2] = "X"
print(it_companies)

# 11. Agrega una empresa IT a it_companies
it_companies.append("GitHub")
print(it_companies)

# 12. Inserta una empresa IT en la mitad de la lista
it_companies.insert(4, "Nvidia")
print(it_companies)

# 13. Cambia el nombre de una empresa en it_companies a mayúsculas (¡excepto IBM!)
it_companies[4] = it_companies[4].upper()
print(it_companies)

# 14. Une it_companies en una cadena usando la cadena '#;  '
print("#;  ".join(it_companies))

# 15. Verifica si una empresa existe en it_companies
print("Oracle" in it_companies)

# 16. Ordena la lista usando el método sort()
it_companies.sort()
print(it_companies)

# 17. Invierte la lista en orden descendente usando reverse()
it_companies.reverse()
print(it_companies)

# 18. Corta (slice) las primeras 3 empresas de la lista
print(it_companies[0:3])

# 19. Corta (slice) las últimas 3 empresas de la lista
print(it_companies[-3:])

# 20. Corta la(s) empresa(s) del medio de la lista
print(it_companies[4:5])

# 21. Elimina la primera empresa IT de la lista
it_companies.pop(0)
print(it_companies)

# 22. Elimina la(s) empresa(s) del medio de la lista
# Puedo usar remove("nombre de empresa"), pero que aburrido, ademas no siempre sabré cual es el del medio xd
mid_company = len(it_companies) // 2
del it_companies[mid_company]
print(it_companies)

# 23. Elimina la última empresa IT de la lista
it_companies.pop()
print(it_companies)

# 24. Elimina todas las empresas IT de la lista
it_companies.clear()
print(it_companies)

# 25. Destruye la lista it_companies
del it_companies

# 26. Concatena las siguientes listas:
#     front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#     back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
front_end.extend(back_end)
print(front_end)

# 27. Inserta 'Python' y 'SQL' después de full_stack en la lista concatenada.
full_stack.extend(["Python", "SQL"])
print(full_stack)
full_stack[5:5] = ["Tailwind", "Springboot"]
print(full_stack)

# Ejercicios: Nivel 2

# 1. A continuación, una lista con las edades de 10 estudiantes:
#    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#      Ordena la lista y encuentra la edad máxima y mínima
#      Agrega la edad mínima y máxima nuevamente a la lista
#      Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
#      Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
#      Encuentra el rango de edades (máximo - mínimo)
#      Compara |min - promedio| y |max - promedio| usando la función abs()
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"Edad minima: {ages[0]}\nEdad maxima: {ages[-1]}")
ages.insert(0, ages[0])
ages.append(ages[-1])
print(ages)
median = (ages[(len(ages) - 1) // 2] + ages[(len(ages) // 2)]) / 2
print(f"La mediana es: {median}")
promedio = sum(ages) / len(ages)
print(f"El promedio es: {promedio}")
print(f"El rango de edades es: {max(ages) - min (ages)}")
print(
    f"|min - promedio|: {abs(min(ages) - promedio)}\n|max - promedio|: {abs(max(ages) - promedio)}")

# 1. Encuentra el país del medio en la lista de países
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]
mid_country = len(countries) // 2
print(countries[mid_country])

# 2. Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
print(countries[:mid_country + 1])
print(countries[mid_country + 1:])

# 3. Para la lista ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'], separa los tres primeros países de los países nórdicos restantes.
countries_list = ['China', 'Russia', 'USA',
                  'Finland', 'Sweden', 'Norway', 'Denmark']
first_three_countries = countries_list[0:3]
nordic_countries = countries_list[3:]
print(first_three_countries)
print(nordic_countries)
