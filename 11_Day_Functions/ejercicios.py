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


# 4. Escribe distintas funciones que acepten listas y calculen: media, mediana, moda, rango, varianza y desviación estándar.


