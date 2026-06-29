# Ejercicios: Nivel 1
# 1. Declara una función add_two_numbers. Debe aceptar dos parámetros y devolver su suma.
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total

print(add_two_numbers(1, 2))

# 2. La fórmula del área de un círculo es: area = π x r x r. Escribe una función area_of_circle que la calcule.
def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area

print(area_of_circle(10))

# 3. Escribe una función llamada add_all_nums que acepte un número arbitrario de argumentos y sume todos. Verifica que todos los elementos sean de tipo numérico. Si no, devuelve un mensaje apropiado.
def add_all_nums(*num):
    total = 0
    
    for n in num:
        if type(n) == int or type(n) == float:
            total += n
        else:
            return "Error: Todos los elementos deben ser numéricos."
    
    return total

print(add_all_nums(1,2,3, "4"))

# 4. La temperatura en Celsius (°C) se puede convertir a Fahrenheit (°F) con: °F = (°C x 9/5) + 32. Escribe una función convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

print(convert_celsius_to_fahrenheit(10))

# 5. Escribe una función llamada check_season que acepte un mes y devuelva la estación: otoño, invierno, primavera o verano.
mes = input("Ingrese un mes: ").capitalize()

def check_season(mes):
    if mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
        return "Otoño"
    elif mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
        return "Invierno"
    elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
        return "Primavera"
    elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
        return "Verano"
    else:
        return "Ingrese un mes válido"

print(check_season(mes))

# 6. Escribe una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal.
def calculate_slope(x1, x2, y1, y2):
    pendiente = (y2-y1)/(x2-x1)
    if x2-x1 == 0:
        return "Error, no se puede dividir entre 0"
    
    return pendiente

print(calculate_slope(3 , 1, 7, 2))

# 7. La ecuación cuadrática se calcula como: ax² + bx + c = 0. Escribe una función solve_quadratic_eqn que calcule las soluciones.
def solve_quadratic_eqn(a, b, c):
    disc = (b ** 2) - (4 * a * c)
    
    if disc < 0:
        return "Error: La ecuación no tiene soluciones reales (raíz negativa)."
    
    raiz = disc ** 0.5
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    
    return x1, x2
        
print(solve_quadratic_eqn(3, 5, 1))

# 8. Declara una función llamada print_list que acepte una lista y imprima cada elemento.
l = [1, "a", 2, "b", 3, "c"]
def print_list(l):
    for element in l:
        print(element)

print_list(l)

# 9. Declara una función llamada reverse_list que acepte un arreglo y devuelva su reverso (usa un bucle).
#    print(reverse_list([1, 2, 3, 4, 5]))
#     [5, 4, 3, 2, 1]
#    print(reverse_list1(["A", "B", "C"]))
#     ["C", "B", "A"]
def reverse_list(l):
    rev_l = []
    for element in range(len(l)-1, -1, -1):
        rev_l.append(l[element])
    return rev_l
    
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10. Declara una función capitalize_list_items que acepte una lista y devuelva una lista con los elementos en mayúscula.
def capitalize_list_items(cl):
    cap_l = []
    for element in cl:
        cap_l.append(element.upper())
    return cap_l
    
print(capitalize_list_items(["alejandro", "martin", "ruidias", "luyo"]))


# 11. Declara una función add_item que acepte una lista y un ítem. Debe devolver la lista con el ítem agregado al final.
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#     print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#     numbers = [2, 3, 7, 9];
#     print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9];
def add_item(l, i):
    return l + [i]

print(add_item(food_staff, 'Meat'))
print(add_item(numbers, 5)) 

# 12. Declara una función remove_item que acepte una lista y un ítem. Debe devolver la lista con el ítem eliminado.
#     food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#     print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
#     numbers = [2, 3, 7, 9];
#     print(remove_item(numbers, 3))  # [2, 7, 9]
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2, 3, 7, 9];
def remove_item(l: list, i):
    copy_l = l.copy()
    copy_l.remove(i)
    return copy_l

print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))

# 13. Declara una función sum_of_numbers que acepte un número y sume todos los números en ese rango.
#     print(sum_of_numbers(5))  # 15
#     print(sum_all_numbers(10)) # 55
#     print(sum_all_numbers(100)) # 5050
def sum_of_numbers(n):
    tot = 0
    for num in range(n + 1):
        tot += num
    return tot
    # return (n * (n + 1)) // 2   <-- Version optimizada, resolvería incluso suma de millones en 1ms, no necesita bucles
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14. Declara una función sum_of_odds que acepte un número y sume todos los impares en ese rango.
def sum_of_odds(n):
    tot = 0
    for num in range(1, n + 1, 2):
        tot += num

    return tot
print(sum_of_odds(7))

# 15. Declara una función sum_of_even que acepte un número y sume todos los pares en ese rango.
def sum_of_even(n):
    tot = 0
    for num in range(0, n + 1, 2):
        tot += num
    return tot
print(sum_of_even(8))


# Ejercicios: Nivel 2
# 1. Declara una función evens_and_odds que acepte un entero positivo y calcule la cantidad de pares e impares en ese número.
#       print(evens_and_odds(100))
#         La cantidad de números pares es 50.
#         La cantidad de números impares es 50.
def evens_and_odds(n):
    odds_tot = 0
    even_tot = 0
    if n > 0:
        for i in range(1, n + 1):
            if i % 2 != 0:
                odds_tot += 1
            else:
                even_tot +=1
        return f"La cantidad de números pares es {even_tot}.\nLa cantidad de números impares es {odds_tot}." 
    else:
        return "Ingrese un número positivo"
    

print(evens_and_odds(100))

# 2. Llama a tu función factorial que acepte un entero y devuelva su factorial.
def factorial(n):
    f = 1
    for num in range(1, n + 1):
        f *= num
    return f
print(factorial(5))

# 3. Llama a tu función is_empty que acepte un argumento y verifique si está vacío.
def is_empty(a):
    return not a   # 'not a' será True si 'a' está completamente vacío (sea string, lista, dicc, etc.)
        
# Pruebas de fuego de nivel profesional:
print(is_empty(""))      # True (String vacío)
print(is_empty([]))      # True (Lista vacía)
print(is_empty({}))      # True (Diccionario vacío)
print(is_empty("hola"))  # False (Tiene texto)
print(is_empty([1, 2]))  # False (Tiene elementos)


# 4. Escribe distintas funciones que acepten listas y calculen: media, mediana, moda, rango, varianza y desviación estándar.
def media(l: list):
    return sum(l) / len(l)

def mediana(l: list):
    ord_l = sorted(l)
    n = len(ord_l)
    if n % 2 == 0:
        i_izq = (n - 1) // 2
        i_der = n // 2
        c = (ord_l[i_izq] + ord_l[i_der]) / 2
    else:
        c = ord_l[n // 2]
    return float(c)

def moda(l: list):
    numero_moda = l[0]
    maximo_repeticiones = 0
    for num in l:
        conteo_actual = l.count(num)
        if conteo_actual > maximo_repeticiones:
            maximo_repeticiones = conteo_actual
            numero_moda = num
        
    return numero_moda

def rango(l):
    return max(l) - min(l)

def varianza(l):
    m = sum(l) / len(l)
    dif_sqrt_acumulada = 0
    for num in l:
        dif_sqrt_acumulada += (num - m) ** 2
    v = dif_sqrt_acumulada / len(l)
        
    return v

def desv_standar(f):
    return f ** 0.5
    
print(media([1,4,3,2,5]))
print(mediana([6,1,4,3,2,5]))
print(moda([1,2,3,6,7,3,2,5,2,1,2,1,3,5,2,4,1,1,1]))
print(rango([1,2,6,8,4,3,9,3]))
print(varianza([1,2,2,4,6]))
print(desv_standar(varianza([1,2,2,4,6])))


#  Ejercicios: Nivel 3
# 1. Escribe una función is_prime que verifique si un número es primo.
def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
        
print(f"¿Es primo? {is_prime(-11)}")


# 2. Escribe una función que verifique si todos los ítems en una lista son únicos.
def es_unico(l: list):
    c_elem = set()
    for element in l:
        if element not in c_elem:
            c_elem.add(element)
        else:
            return False
    return True
    #return len(l) == len(set(l)) <-- Los sets no permiten duplicados, si son del mismo tamaño, entonces todos los items son unicos
    
print(es_unico([1,2,3,4,5,2,3]))

# 3. Escribe una función que verifique si todos los ítems en una lista son del mismo tipo de dato.
def data_type_is_uni(l: list):
    dat_typ_ref = type(l[0])
    for element in l:
        if type(element) != dat_typ_ref:
            return False
    return True

print(data_type_is_uni([1,"Alejandro", True, 2,3]))

# 4. Escribe una función que verifique si una variable proporcionada es un nombre de variable válido en Python.
import keyword

def var_valida(v):
    if v.isidentifier() and not keyword.iskeyword(v):
        return True
    else:
        return False

# Pruebas de fuego:
print(var_valida("Hola_Mundo")) # True (Limpio)
print(var_valida("1_variable")) # False (Empieza con número, detectado por .isidentifier)
print(var_valida("def"))        # False (Palabra reservada, detectado por keyword)

# 5. Accede al archivo de datos countries-data.py.
import data.countries_data as cd
#     Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
def the_most_spoken_languages(n):
    lang_list = []
    for country in cd.countries_list:
        lang_country = country["languages"]
        for lang in lang_country:
            lang_list.append(lang)
    
    count_lang = dict()
    for lang in lang_list:
        if lang not in count_lang:
            count_lang[lang] = 1
        else:
            count_lang[lang] += 1
    
    ord_lang = sorted(count_lang.values(), reverse=True)[:n]
    count_lang_copy = count_lang.copy() 
    
    most_spok_lang = dict()
    for cant in ord_lang:
        for key, value in list(count_lang_copy.items()):
            if value == cant:
                most_spok_lang[key] = cant
                del count_lang_copy[key]
                break
    
    return most_spok_lang

print(the_most_spoken_languages(20))


#     Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.