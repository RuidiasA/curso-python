# fmt: off
import sys
import os
# Este truco le dice a Python: "Oye, agrega la carpeta raíz al mapa para que encuentres los archivos"
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import data.countries as c
import data.countries_data as cd
# fmt: on

# Ejercicios: Nivel 1
# 1. Implementa iteraciones de 0 a 10 usando while y for.
n = 0

print("While:")
while n < 11:
    print(n)
    n += 1

print("For:")
for n in range(11):
    print(n)

# 2. Implementa iteraciones de 10 a 0 usando while y for.
n_inv = 10

print("While:")
while n_inv >= 0:
    print(n_inv)
    n_inv -= 1

print("For:")
for n in range(10, -1, -1):
    print(n)


# 3. Escribe un bucle que llame a print() 7 veces para producir este triángulo:
    #
    ##
    ###
    ####
    #####
    ######
    #######
h = "#"
for i in range(1, 8):
    print(h*i)

# 4. Usa bucles anidados para producir la siguiente salida:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print(" ")

# 5. Usando un bucle, produce la siguiente salida:
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
for i in range(11):
    print(f"{i} x {i} = {i ** 2}")

# 6. Recorre con for la lista ['Python', 'Numpy','Pandas','Django', 'Flask'] e imprime cada elemento.
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for element in lst:
    print(element)

# 7. Recorre con for de 0 a 100 e imprime todos los números pares.
for n in range(0, 101, 2):
    print(n)

# 8. Recorre con for de 0 a 100 e imprime todos los números impares.
for n in range(1, 101, 2):
    print(n)


# Ejercicios: Nivel 2
# 1. Usa un for para sumar los números de 0 a 100.
#    The sum of all numbers is 5050.
cont = 0
for n in range(101):
    cont += n
print(f"The sum of all numbers is {cont}")

# 2. Usa un for para sumar por separado los impares y los pares de 0 a 100.
#    The sum of all odd numbers is 2500. And the sum of all even numbers is 2550.
c_imp = 0
c_par = 0
for n in range(101):
    if n % 2 != 0:
        c_imp += n
    else:
        c_par += n
print(
    f"The sum of all odd numbers is {c_imp}. And the sum of all even numbers is {c_par}.")


# Ejercicios: Nivel 3
# 1. Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
for country in c.countries:
    if "land" in country.lower():
        print(country)

# 2. Dada la lista fruits = ['banana', 'orange', 'mango', 'lemon'], invierte los elementos usando un bucle.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []
for i in range(len(fruits) - 1, -1, -1):
    fruits_reverse.append(fruits[i])
print(fruits_reverse)

# 3. Ve a la carpeta data y usa el archivo countries-data.py.
#      i. ¿Cuántos idiomas distintos hay en los datos?
idiomas_unicos = set()
for country in cd.countries_list:
    lista_idiomas = country["languages"]
    idiomas_unicos.update(lista_idiomas)
print(idiomas_unicos)
print(f"En total hay {len(idiomas_unicos)} idiomas distintos en los datos.")

#     ii. ¿Cuál es el idioma usado por más países?
lang = list()
for country in cd.countries_list:
    lang_list = country["languages"]
    for i in lang_list:
        lang.append(i)
# print(lang)

count_lang = dict()
for l in lang:
    if l not in count_lang:
        count_lang[l] = 1
    else:
        count_lang[l] += 1
# print(count_lang)

max_lang = ""
max_qnt = 0
for i, q in count_lang.items():
    # print(i, q)
    if q > max_qnt:
        max_lang = i
        max_qnt = q

print(max_lang, max_qnt)

#    iii. Encuentra los diez países con mayor población.
most_pop_countries = []
for country in cd.countries_list:
    if len(most_pop_countries) < 10:
        most_pop_countries.append((country["population"], country["name"]))
        most_pop_countries.sort(reverse=True)
    elif country["population"] > most_pop_countries[-1][0]:
        most_pop_countries[-1] = (country["population"], country["name"])
        most_pop_countries.sort(reverse=True)

for rank, (pop, name) in enumerate(most_pop_countries, 1):
    print(f"{rank}. {name} - Población: {pop:,}")
