"""Ejercicios de práctica"""
"""
Ejercicios: Nivel 1
Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
Declarar una variable de nombre y asignarle un valor
Declarar una variable de apellido y asignarle un valor
Declare una variable de nombre completo y asígnele un valor
Declarar una variable de país y asignarle un valor
Declarar una variable de ciudad y asignarle un valor
Declarar una variable de edad y asignarle un valor
Declarar una variable de año y asignarle un valor
Declarar una variable is_married y asignarle un valor
Declarar una variable is_true y asignarle un valor
Declare una variable is_light_on y asígnele un valor
Declarar múltiples variables en una línea
"""

nombre = "Alejandro"
apellido = "Ruidias"
nombre_completo = nombre + " " + apellido
pais = "Peru"
ciudad = "Lima"
edad = 23
anio = 2026
is_married = False
is_true = True
is_light_on = False

nombre, apellido, parentezco, edad = "Carlos", "Ruidias", "Hermano", 26


"""
Ejercicios: Nivel 2
Verifique el tipo de datos de todas sus variables usando la función incorporada type()
Usando la función incorporada len(), encuentre la longitud de su nombre
Compara la longitud de tu nombre y tu apellido
Declarar 5 como num_one y 4 como num_two
Sume num_one y num_two y asigne el valor a un total variable
Reste num_two de num_one y asigne el valor a una variable diff
Multiplique num_two y num_one y asigne el valor a un producto variable
Divide num_one por num_two y asigna el valor a una división variable
Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
El radio de un círculo es de 30 metros.
Calcule el área de un círculo y asigne el valor a una variable con el nombre de area_of_circle
Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de circum_of_circle
Tome el radio como entrada del usuario y calcule el área.
Use la función de entrada integrada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras o palabras clave reservadas de Python
"""


print("Nombre:", type(nombre))
print("Apellido:", type(apellido))
print("Nombre completo:", type(nombre_completo))
print("Pais:", type(pais))
print("Ciudad:", type(ciudad))
print("Edad:", type(edad))
print("Anio:", type(anio))
print("Esta casado:", type(is_married))
print("Es verdad:", type(is_true))
print("Luz encendida:", type(is_light_on))
print("Parentezco:", type(parentezco))

print("Longitud del nombre: ", len(nombre))

print(len(nombre) == len(apellido))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
producto = num_one * num_two
division = num_one / num_two
residuo = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radio = 30
PI = 3.14159
area_of_circle = PI * radio * radio
circum_of_circle = 2 * PI * radio
print("El area del circulo es:", area_of_circle)
print("La circunferencia del circulo es:", circum_of_circle)


radio_usuario = float(input("Ingrese el radio de la circunferencia: "))
area_of_circle = PI * radio_usuario * radio_usuario

print("El area del circulo es: ", area_of_circle)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su pais: ")
edad = input("Ingrese su edad: ")

print(nombre, apellido, pais, edad)

help('keywords')
