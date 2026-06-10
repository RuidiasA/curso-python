fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # devuelve todos los elementos
# mismo resultado que arriba
# Si no se especifica el índice de fin, devolverá todos los elementos desde el inicio hasta el final
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]  # no incluye el índice 3
orange_mango_lemon = fruits[1:]
# usamos el tercer parámetro (paso). Toma cada 2 elementos - ['banana', 'mango']
orange_and_lemon = fruits[1::2]

print(orange_and_lemon)
