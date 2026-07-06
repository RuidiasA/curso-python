# 4. Imprime cada país de la lista countries usando un bucle for.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# 5. Imprime cada nombre de la lista names usando un bucle for.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# 6. Imprime cada número de la lista numbers usando un bucle for.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ejercicios: Intermedio
# 1. Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista.
countries_upper = list(map(lambda c : c.upper(), countries))
print(countries_upper)

# 2. Usa map para elevar al cuadrado cada número en numbers y genera una nueva lista.
pow_num = list(map(lambda n : n ** 2, numbers))
print(pow_num)

# 3. Usa map para convertir cada nombre en names a mayúsculas y genera una nueva lista.
names_upper = list(map(lambda n : n.upper(), names))
print(names_upper)

# 4. Usa filter para filtrar países que contienen 'land'.
land_filt = list(filter(lambda c : "land" in c, countries))
print(land_filt)

# 5. Usa filter para filtrar países con exactamente seis caracteres.
count_6 = list(filter(lambda c : len(c) == 6, countries))
print(count_6)

# 6. Usa filter para filtrar países con seis o más caracteres.
count_m6 = list(filter(lambda c : len(c) >= 6, countries))
print(count_m6)

# 7. Usa filter para filtrar países que comienzan con 'E'.
cont_e = list(filter(lambda c : c[0] == "E", countries))
print(cont_e)

# 8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).


# 9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los countrieos de tipo cadena.


# 10. Usa reduce para sumar todos los números en la lista numbers.