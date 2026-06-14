# Ejercicios - Día 7
# Conjuntos
#   it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#   A = {19, 22, 24, 20, 25, 26}
#   B = {19, 22, 20, 25, 26, 24, 28, 27}
#   age = [22, 19, 24, 25, 26, 24, 25, 24]


#   Ejercicios: Nivel 1
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
#   1. Encuentra la longitud del conjunto it_companies
print(len(it_companies))

#   2. Agrega 'Twitter' a it_companies
it_companies.add("Twitter")
print(it_companies)

#   3. Inserta varias empresas IT a it_companies de una sola vez
it_companies.update(["Nvidia", "Instagram", "Intel"])
print(it_companies)

#   4. Elimina una empresa de it_companies
it_companies.pop()  # pop para eliminar un elemento aleatorio
print(it_companies)

#   5. ¿Cuál es la diferencia entre remove() y discard()?
it_companies.discard("IBM")
print("IBM eliminado con .discard() por primera vez:", it_companies)
it_companies.discard("IBM")
# discard() no dará error aunque el elemento a eliminar no exista
print("IBM eliminado con .discard() por segunda vez:", it_companies)

it_companies.remove("Facebook")
print("Facebook eliminado con .remove() por primera vez:", it_companies)
"""
COMENTADO PARA NO CORTAR LA EJECUCION XD
it_companies.remove("Facebook")
# .remove() mostrará un mensaje de error porque el elemento a eliminar no existe y detendrá el programa
print("Facebook eliminado con .remove() por segunda vez:", it_companies)
"""


# Ejercicios: Nivel 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# 1. Concatena A y B
print("Union:", A.union(B))  # .union() devuelve un nuevo conjunto
A.update(B)  # .update() inserta los elementos en el conjunto
print("Update:", A)
# En ambos casos al concatenar "conjuntos" o "sets", devuelve todos los elementos encontrados pero solo una vez por elemento

# 2. Encuentra la intersección entre A y B
# Asigno de nuevo los valores iniciales al conjunto A porque fue modificado xdd
A = {19, 22, 24, 20, 25, 26}
# .intersection() devuelve los elementos que se encuentran en ambos conjuntos
print("Interseccion:", A.intersection(B))

# 3. ¿Es A un subconjunto de B?
print("¿Es A un subconjunto de B?", A.issubset(B))

# 4. ¿Son A y B conjuntos disjuntos?
print("¿Son A y B conjuntos disjuntos?", A.isdisjoint(B))

# 5. Combina A con B y viceversa
print("A unido a B", A.union(B))
print("B unido a A", B.union(A))

# 6. ¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))

"""
# 7. Elimina un conjunto por completo
del B
print(B)  # Esto debe dar error porque B no fue definido
"""


# Ejercicios: Nivel 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Convierte la lista de edades a un conjunto y compara la longitud de la lista y la del conjunto: ¿cuál es mayor?
age_set = set(age)
print(f"Longitud de la lista: {len(age)}\nLongitud del conjunto: {len(age_set)}\n¿La longitud de la lista es mayor que la del conjunto? {len(age) > len(age_set)}")

# 2. Explica la diferencia entre estos tipos de datos: cadena, lista, tupla y conjunto
# string: es una cadena de caracteres unicode, puede almacenar cualquier tipo de objeto, es inmutable y ordenada (indexable), permite elementos duplicados | sintaxis: "texto" o 'texto'
# list: es mutable y ordenada (indexable), permite elementos duplicados | sintaxis: [1, 2, 3]
# tuple: es inmutable y ordenada (indexable), permite elementos duplicados | sintaxis: (1, 2, 3)
# set: es mutable, desordenada (no indexable), no permite elementos duplicados | sintaxis: {1, 2, 3}

# 3. Para la frase "Soy profesor, me gusta motivar y enseñar a las personas." ¿cuántas palabras únicas tiene? Usa split() y conjuntos para obtener las palabras únicas.
frase = "Soy profesor, me gusta motivar y enseñar a las personas."
frase_normalizada = frase.replace(",", "").replace(".", "").lower()

palabras = frase_normalizada.split()
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)
print(len(palabras_unicas))
