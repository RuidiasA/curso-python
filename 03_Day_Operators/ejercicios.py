# Declara tu edad como variable entera
age = 23
print("Edad:", age)

# Declara tu altura como una variable flotante
height = 1.70
print("Altura:", height)

# Declarar una variable que almacene un número complejo
complex_num = 1 + 1j
print("Numero complejo:", complex_num)

# Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 x b x h).
b = input("Ingresa la base del triangulo: ")
h = input("Ingresa la altura del triangulo: ")
area_of_triangle = float(b) * float(h) / 2
print("Area del triangulo: ", area_of_triangle)

# Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo
a = input("Ingrese el primer lado del triangulo, a: ")
b = input("Ingrese el primer lado del triangulo, b: ")
c = input("Ingrese el primer lado del triangulo, c: ")
perimetro_triangulo = float(a) + float(b) + float(c)
print("Perimetro del triangulo: ", perimetro_triangulo)


# Obtenga la longitud y el ancho de un rectángulo usando el indicador. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
largo = float(input("Ingrese el largo del rectangulo: "))
ancho = float(input("Ingrese el ancho del rectangulo: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = (largo + ancho) * 2
print("Area del rectangulo: ", area_rectangulo)
print("Perimetro del rectangulo: ", perimetro_rectangulo)

# Obtenga el radio de un círculo usando el aviso. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
r = float(input("Ingrese el radio del circulo: "))
area = 3.14 * (r ** 2)
circunferencia = 2 * 3.14 * r
print("Area del circulo:", area)
print("Circunferencia del circulo:", circunferencia)

# Calcular la pendiente, la intersección x y la intersección y de y = 2x -2
# y = mx + b
# y = 2x - 2
m = 2
b = -2
inters_y = m * 0 + b
# 0 = 2x - 2
inters_x = -b / m
print(f"Pendiente: {m}")
print(f"Interseccion Y: (0, {inters_y})")
print(f"Interseccion X: ({inters_x}, 0)")

# La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la distancia euclidiana entre el punto (2, 2) y el punto (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente = (y2 - y1) / (x2 - x1)
print(f"La pendiente es: {pendiente}")
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"La distancia euclidiana es: {d:.2f}")

# Compara las pendientes en las tareas 8 y 9.
print(m == pendiente)

# Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0.
x_3 = -3
y_3 = (x_3**2) + (6*x_3) + 9
x_2 = -2
y_2 = (x_2**2) + (6*x_2) + 9
x_1 = -1
y_1 = (x_1**2) + (6*x_1) + 9
x0 = 0
y0 = (x0**2) + (6*x0) + 9
x1 = 1
y1 = (x1**2) + (6*x1) + 9
print("y(-3):", y_3)
print("y(-2):", y_2)
print("y(-1):", y_1)
print("y(0):", y0)
print("y(1):", y1)

# Encuentra la longitud de 'python' y 'dragon' y haz una declaración de comparación falsa.
l_python = len("python")
l_dragon = len("dragon")
print(f"Longitud de python: {l_python}")
print(f"Longitud de dragon: {l_dragon}")
print(f"¿Longitudes iguales?: {l_python == l_dragon}")

# Use el operador and para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
print("on in (python) and (dragon):", "on" in "python" and "on" in "dragon")

# Espero que este curso no esté lleno de jerga. Use el operador in para verificar si jerga está en la oración.
print("jerga in (Espero que este curso no esté lleno de jerga):",
      "jerga" in "Espero que este curso no esté lleno de jerga")

# No hay 'on' ni en dragón ni en pitón
print(not "on" in "dragón" and not "on" in "pitón")

# Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en cadena
print(f"Longitud de python: {l_python}")
print(f"Float: {float(l_python)}")
print(f"String: {str(l_python)}")

# Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
num = float(input("Ingrese un numero: "))
print(f"¿El numero es par?: {num % 2 == 0}")

# Verifique si la división de piso de 7 por 3 es igual al valor int convertido de 2.7.
floor_div = 7 // 3
num_int = int(2.7)
print(f"¿{floor_div} es igual a {num_int}?: {floor_div == num_int}")

# Comprueba si el tipo de '10' es igual al tipo de 10
print(type("10") == type(10))

# Comprueba si int('9.8') es igual a 10
print(int(9.8) == 10)

# Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?
horas = int(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese las tarifa por hora: "))
print(f"El salario es: {horas * tarifa}")

# Escriba un script que le solicite al usuario que ingrese el número de años. Calcula el número de segundos que una persona puede vivir. Suponga que una persona puede vivir cien años.
years = int(input("Ingrese el numero de años vividos: "))
seconds = years * 365 * 24 * 60 * 60
print(f"Viviste {seconds} segundos")

"""
Escriba un script de Python que muestre la siguiente tabla:
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print(
    f"1 1 1 {1**2} {1**3}\n"
    f"2 1 2 {2**2} {2**3}\n"
    f"3 1 3 {3**2} {3**3}\n"
    f"4 1 4 {4**2} {4**3}\n"
    f"5 1 5 {5**2} {5**3}"
)
