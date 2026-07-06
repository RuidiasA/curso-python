# Ejercicios: Día 14
# Ejercicios: Básico
# 1. Explica la diferencia entre map, filter y reduce.
"""
map es una funcion integrada que recibe una funcion y un iterable como parametros, nos permite aplicar una funcion a cada elemento de un objeto iterable sin necesidad de usar bucles
map: Transforma todos los elementos de un iterable (Entran N elementos, salen N elementos modificados).

filter es una función que recibe otra función (la cual devuelve un booleano) para filtrar un iterable, devolviendo un nuevo iterable solo con los elementos que dieron True". 
filter: Selecciona elementos basados en una condición lógica (Entran N elementos, sale una cantidad menor o igual a N).

reduce es una funcion que devuelve un valor acumulado, reduce no opera de golpe, sino que aplica la función en parejas de elementos, de izquierda a derecha, hasta que solo queda un único valor.
reduce: Combina/Acumula todos los elementos en cadena hasta colapsarlos en un solo valor final.
"""

# 2. Explica la diferencia entre funciones de orden superior, closures y decoradores.
"""
Las funciones de orden superior son funciones que contienen otra funcion, puede recibir una o mas funciones como parametros, pueden ser modificadas, asignarse a una variable, ser el valor de retorno de otra funcion
Función de Orden Superior: Es el concepto general (funciones que juegan con otras funciones como si fueran variables).

El closure es un contenedor que permite devolver la funcion que se envuelve
Closure: Es el mecanismo de memoria (la función de adentro recuerda las cosas de la función de afuera).

Los decoradores premiten darle una funcionalidad a una funcion sin modificar su estructura, en la práctica, es una función de orden superior especializada que toma una función como argumento, la envuelve usando un closure, y devuelve una nueva versión modificada de esa función.
Decorador: Es la aplicación práctica (usar el concepto general y la memoria para envolver una función con el @ y meterle superpoderes sin romper su estructura).
"""

# 3. Define la función que llama (ver ejemplo).
total_gastos = 0

def gastos_diarios(g):
    global total_gastos
    total_gastos += g
    
    return total_gastos

def gasto(func, prec_prod):
    gast = func(prec_prod)
    return gast
#   return func(prec_prod)  <-- version mas corta sin declarar una variable innecesariamente en este caso

print(gasto(gastos_diarios, 3.5))
print(gasto(gastos_diarios, 12.00))
print(gasto(gastos_diarios, 5.00))

# 4. Imprime cada país de la lista countries usando un bucle for.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

for country in countries:
    print(country)

# 5. Imprime cada nombre de la lista names usando un bucle for.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

for name in names:
    print(name)

# 6. Imprime cada número de la lista numbers usando un bucle for.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)


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
cont_e = list(filter(lambda c : c.startswith("E"), countries))
print(cont_e)

# 8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).
cad = list(map(lambda e : e ** 2 ,filter(lambda n : n % 2 ==0, numbers)))
print(cad)

# 9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.
def get_string_lists(l: list):
    str_elem = list(filter(lambda s : isinstance(s, str), l))
    return str_elem

print(get_string_lists(["Perú", 23, "Argentina", True, 3.5, "Brasil"]))

# 10. Usa reduce para sumar todos los números en la lista numbers.
from functools import reduce

sum_num = reduce(lambda n1, n2 : n1 + n2, numbers)
print(sum_num)

# 11. Usa reduce para concatenar todos los países en una oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
first_count = reduce(lambda acc, c: f"{acc}, {c}", countries[:-1])
sentence = f"{first_count} and {countries[-1]} are north European countries."
print(sentence)

# 12. Declara una función categorize_countries que retorne una lista de países que siguen un patrón común (puedes ver la lista de países en el archivo countries.js del repositorio, por ejemplo 'land', 'ia', 'island', 'stan').
import data.countries as dc

def categorize_countries(l: list):
    land_countries = list(filter(lambda c : "land" in c, l))
    return land_countries

print(categorize_countries(dc.countries))

# 13. Crea una función que devuelva un diccionario donde las claves sean la primera letra de los nombres de país y el valor sea el número de países que comienzan con esa letra.
def count_countries_by_letter(country_list: list):
    def update_letter_counts(letter_counts, country):
        first_letter = country[0]
        
        if first_letter not in letter_counts:
            letter_counts[first_letter] = 1
        else:
            letter_counts[first_letter] += 1
            
        return letter_counts
    
    return reduce(update_letter_counts, country_list, {})

print(count_countries_by_letter(dc.countries))

# 14. Declara una función get_first_ten_countries que devuelva los primeros diez países de la lista countries.js en la carpeta data.


# 15. Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista.



# Ejercicios: Avanzado
# Usando el archivo countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py), completa lo siguiente:
#   Ordena los países por nombre, capital y población.
#   Ordena y obtiene los diez idiomas más usados.
#   Ordena y obtiene los diez países con mayor población.