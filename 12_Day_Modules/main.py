import mymodule

print(mymodule.generate_full_name("Alejandro", "Ruidias"))


from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])


from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])


# ----- MODULO OS -----
import os
# crear directorio
os.mkdir("directory_name")
# cambiar el directorio actual
os.chdir('path')
# obtener el directorio actual
os.getcwd()
# eliminar directorio
os.rmdir()


# ----- MODULO SYS -----
import sys
# salir del script
sys.exit()
# conocer el tamaño máximo de un entero
sys.maxsize
# conocer la ruta de módulos
sys.path
# conocer la versión de Python en uso
sys.version


# ----- MODULO STATISTICS -----
from statistics import * # importar todo del módulo statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3


# ----- MODULO MATH -----
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raíz cuadrada
print(math.pow(2, 3))    # 8.0, potencia
print(math.floor(9.81))  # 9, redondeo hacia abajo
print(math.ceil(9.81))   # 10, redondeo hacia arriba
print(math.log10(100))   # 2, logaritmo base 10

# Si sólo queremos importar funciones específicas podemos hacerlo así:
from math import pi
print(pi)

# También podemos importar múltiples funciones:
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# Si queremos importar todas las funciones del módulo matemático podemos usar *.
from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, raíz cuadrada
print(pow(2, 3))           # 8.0, potencia
print(floor(9.81))         # 9, redondeo hacia abajo
print(ceil(9.81))          # 10, redondeo hacia arriba
print(math.log10(100))     # 2

# También podemos renombrar funciones al importarlas.
from math import pi as PI
print(PI) # 3.141592653589793


# ----- MODULO STRING -----
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


# ----- MODULO RANDOM -----
from random import random, randint
print(random())   # no necesita parámetros; devuelve un valor entre 0 y 0.9999
print(randint(5, 20)) # devuelve un entero aleatorio en [5, 20] (inclusive)