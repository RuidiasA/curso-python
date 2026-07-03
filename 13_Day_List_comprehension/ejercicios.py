# Ejercicios: Día 13
# 1. Usa una comprensión de listas para filtrar los números negativos y ceros de la siguiente lista:
#       numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numb_filt = [num for num in numbers if num > 0]

print(numb_filt)

# 2. Aplana la siguiente lista de listas a una lista unidimensional:
#       list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#       Salida:
#       [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

unidim_list = [num for bloque in list_of_lists for row in bloque for num in row]

print(unidim_list)

# 3. Crea la siguiente lista de tuplas usando una comprensión de listas:
#       [(0, 1, 0, 0, 0, 0, 0),
#        (1, 1, 1, 1, 1, 1, 1),
#        (2, 1, 2, 4, 8, 16, 32),
#        (3, 1, 3, 9, 27, 81, 243),
#        (4, 1, 4, 16, 64, 256, 1024),
#        (5, 1, 5, 25, 125, 625, 3125),
#        (6, 1, 6, 36, 216, 1296, 7776),
#        (7, 1, 7, 49, 343, 2401, 16807),
#        (8, 1, 8, 64, 512, 4096, 32768),
#        (9, 1, 9, 81, 729, 6561, 59049),
#        (10, 1, 10, 100, 1000, 10000, 100000)]

tpl_list = [(n, n ** 0, n ** 1, n ** 2, n ** 3, n ** 4, n **5) for n in range(11)]
tpl_list_opt = [tuple([n] + [n ** i for i in range(6)]) for n in range(11)]  # <-- optimizado para obtener cualquier numero y cantidad facilmente

print(*tpl_list_opt, sep="\n")

# 4. Aplana la siguiente estructura en una nueva lista:
#       countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
#       Salida:
#       [['Finlandia', 'FIN', 'Helsinki'], ['Suecia', 'SUE', 'Estocolmo'], ['Noruega', 'NOR', 'Oslo']]
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]

new_coun_list = [[item[0], item[0][:3].upper(), item[1]] for bloque in countries for item in bloque]

print(new_coun_list)

# 5. Convierte la siguiente lista en una lista de diccionarios:
#       countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
#       Salida:
#       [{'País': 'Finlandia', 'Ciudad': 'Helsinki'},
#        {'País': 'Suecia', 'Ciudad': 'Estocolmo'},
#        {'País': 'Noruega', 'Ciudad': 'Oslo'}]
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]

coun_dict = [{"País": i[0], "Ciudad" : i[1]} for bloque in countries for i in bloque]

print(coun_dict)

# 6. Convierte la siguiente lista en una lista de cadenas concatenadas:
#       names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#       Salida:
#       ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_names = [f"{item[0]} {item[1]}" for bloque in names for item in bloque]

print(full_names)

# 7. Escribe una función lambda que calcule la pendiente o la ordenada al origen de una función lineal.

pend = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)

orde = lambda x, y, m : y - (m * x)

print(pend(2, 3, 6, 11))
print(orde(3, 5, 2))