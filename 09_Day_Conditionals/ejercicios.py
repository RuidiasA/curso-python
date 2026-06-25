# Ejercicios: Nivel 1
# 1. Usa input para obtener la edad del usuario (por ejemplo: "Introduce tu edad:"). Si el usuario tiene 18 años o más, muestra: 'Ya tienes la edad suficiente para aprender a conducir.' Si es menor, muestra cuántos años le faltan. Ejemplo de salida:
#    Introduce tu edad: 30
#    Ya tienes la edad suficiente para aprender a conducir.
#    Salida:
#    Introduce tu edad: 15
#    Aún necesitas esperar 3 años para aprender a conducir.
edad = int(input("Introduce tu edad: "))
print("Ya tienes la edad suficiente para aprender a conducir.") if edad >= 18 else print(
    f"Aún necesitas esperar {18 - edad} años para aprender a conducir.")

# 2. Usa if…else para comparar my_age y your_age. ¿Quién es mayor (yo o tú)? Usa input("Introduce tu edad:") para obtener la edad. Puedes usar condicionales anidados para imprimir 'año' cuando la diferencia sea 1, 'años' para diferencias mayores, y un mensaje personalizado si my_age = your_age. Salida de ejemplo:
#    Introduce tu edad: 30
#    Tienes 5 años más que yo.
my_age = 23
your_age = int(input("Inroduce tu edad: "))
dif = abs(your_age - my_age)
time = "años" if dif != 1 else "año"
if your_age > my_age:
    print(f"Tienes {dif} {time} más que yo.")
elif your_age == my_age:
    print("Tenemos la misma edad.")
else:
    print(f"Tienes {dif} {time} menos que yo.")

# 3. Pide al usuario dos números con input. Si a > b, imprime 'a es mayor que b'; si a < b, imprime 'a es menor que b'; si son iguales, imprime 'a es igual a b'.
#    Introduce el primer número: 4
#    Introduce el segundo número: 3
#    4 es mayor que 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print(a, "es igual que", b)


# Ejercicios: Nivel 2
# 1. Escribe un código que asigne una calificación según la nota del estudiante:
#    80-100, A
#    70-79, B
#    60-69, C
#    50-59, D
#    0-49, F
cal_est = int(input("Ingrese la calificación: "))
if 100 >= cal_est >= 80:
    rango = "A"
elif 80 > cal_est >= 70:
    rango = "B"
elif 70 > cal_est >= 60:
    rango = "C"
elif 60 > cal_est >= 50:
    rango = "D"
elif 50 > cal_est >= 0:
    rango = "F"
else:
    rango = "Ingrese una calificación válida (0 - 100)"
print(rango)

# 2. Comprueba si es otoño, invierno, primavera o verano. Si el usuario introduce: Septiembre, Octubre o Noviembre → otoño. Diciembre, Enero o Febrero → invierno. Marzo, Abril o Mayo → primavera. Junio, Julio u Agosto → verano.
mes = input("Ingresa el mes del año: ").capitalize()
if mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
    est = "Otoño"
elif mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
    est = "Invierno"
elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
    est = "Primavera"
elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
    est = "Verano"
else:
    est = "Ingrese un mes válido"
print(est)

# 3. La siguiente lista contiene algunas frutas:
#    fruits = ['banana', 'orange', 'mango', 'lemon']
#    Si una fruta no está en la lista, añádela e imprime la lista modificada. Si ya existe, imprime 'La fruta ya está en la lista'.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Ingresa una fruta: ").lower()
if fruit in fruits:
    print("La fruta ya está en la lista")
else:
    fruits.append(fruit)
    print(fruits)

# Ejercicios: Nivel 3
# 1. Aquí hay un diccionario persona. ¡Siéntete libre de modificarlo!
#    person = {
#        'first_name': 'Asabeneh',
#        'last_name': 'Yetayeh',
#        'age': 250,
#        'country': 'Finlandia',
#        'is_married': True,
#        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#        'address': {
#            'street': 'Calle Espacial',
#            'zipcode': '02210'
#        }
#    }
#    Comprueba si existe la clave skills en el diccionario; si existe, imprime la habilidad central de la lista skills.
#    Comprueba si existe la clave skills; si existe, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
#    Si las habilidades son sólo JavaScript y React, imprime 'Es desarrollador frontend'; si incluyen Node, Python y MongoDB, imprime 'Es desarrollador backend';
#     si incluyen React, Node y MongoDB, imprime 'Es desarrollador full-stack'; en caso contrario, imprime 'Título desconocido' — puedes anidar más condiciones para mayor precisión.
#    Si la persona está casada y vive en Finlandia, imprime la siguiente línea:
#       print('Asabeneh Yetayeh vive en Finlandia. Está casado.')
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}

if "skills" in person:
    l = len(person["skills"])
    print(person["skills"][(l - 1) // 2: l // 2 + 1])

if "skills" in person:
    if "Python" in person["skills"]:
        print("El skill Python existe")

skills_person = set(person["skills"])

if {"React", "Node", "MongoDB"}.issubset(skills_person):
    print("Es desarrollador full-stack")
elif {"Python", "Node", "MongoDB"}.issubset(skills_person):
    print("Es desarrollador backend")
elif {"JavaScript", "React"}.issubset(skills_person):
    print("Es desarrollador frontend")
else:
    print("Título desconocido")

if person["is_married"] and person["country"] == "Finlandia":
    print(f"{person["first_name"]} {person["last_name"]} vive en {person["country"]}. Está casado.")
