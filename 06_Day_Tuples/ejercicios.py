# Ejercicios: Nivel 1
# 1. Crea una tupla vacía
tpl = ()

# 2. Crea una tupla con los nombres de tus hermanos y hermanas (pueden ser ficticios)
tpl_hermanos = ("Diego", "Carlos", "Jorge", "Renzo",
                "Alonso", "Joaquin", "Johan")
tpl_hermanas = ("Alessia", "Danna")

# 3. Concatena las tuplas de hermanos y asígnalas a siblings
siblings = tpl_hermanos + tpl_hermanas

# 4. ¿Cuántos hermanos tienes?
print(len(siblings))

# 5. Modifica la tupla de siblings y añade los nombres de tus padres; asígnala a family_members
print(type(siblings))
family_members = list(siblings)
family_members.append("Giuliana")
family_members.insert(-1, "Carlo")
print("Lista:", family_members)
print(type(family_members))
family_members = tuple(family_members)
print("\nTupla:", family_members)
print(type(family_members))


# Ejercicios: Nivel 2
# 1. Extrae los hermanos y los padres desde family_members
*siblings_ext, father_ext, mother_ext = family_members
print("\nHermanos:", siblings)
parents = (father_ext, mother_ext)
print("Padres:", parents)

# 2. Crea las tuplas fruits, vegetables y animal_products. Concatena las tres tuplas y asígnalas a la variable food_stuff_tp
fruits = ("apple", "pear", "banana", "orange")
vegetables = ("onion", "potato", "tomato", "radish", "beetroot")
animal_products = ("meat", "milk", "eggs", "honey")
food_stuff_tp = fruits + vegetables + animal_products
print("\nConcatenacion de tuplas:", food_stuff_tp)

# 3. Convierte la tupla food_stuff_tp en la lista food_stuff_lt
food_stuff_lt = list(food_stuff_tp)
food_stuff_lt.append("prueba par")
print("Lista:", food_stuff_lt)

# 4. Extrae los elementos del medio desde la tupla food_stuff_tp o la lista food_stuff_lt
t = len(food_stuff_tp)
l = len(food_stuff_lt)
print("Impar:", food_stuff_tp[(t - 1) // 2: t // 2 + 1])
print("Impar:", food_stuff_lt[(l - 1) // 2: l // 2 + 1])

# 5. Extrae las primeras tres y las últimas tres entradas de la lista food_stuff_lt
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

# 6. Elimina completamente la tupla food_stuff_tp
del food_stuff_tp

# 7. Comprueba si existen los elementos:
#    Verifica si 'Estonia' está en la tupla nordic_countries
#    Verifica si 'Iceland' está en la tupla nordic_countries
#    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
