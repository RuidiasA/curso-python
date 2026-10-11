# sintaxis
# open('filename', mode) --> mode(r, a, w, x, t, b) puede ser lectura, escritura o actualización

# "r" - lectura - valor por defecto. Abre el archivo solo para lectura; si no existe genera un error.
# "a" - append (añadir) - abre el archivo para agregar contenido al final; crea el archivo si no existe.
# "w" - escritura - abre el archivo para escribir, sobrescribe si existe; crea el archivo si no existe.
# "x" - crear - crea el archivo; si existe genera un error.
# "t" - texto - valor por defecto. Modo texto.
# "b" - binario - modo binario (por ejemplo para imágenes


# Abrir un archivo para lectura
f = open("./files/reading_file_example.txt")
print(f)
f.close()

# read(): lee todo el texto como una cadena.
# readline(): lee solo la primera línea
# readlines(): lee todo el texto línea por línea y devuelve una lista de líneas
f = open('./files/reading_file_example.txt')
txt = f.read() # --> Podemos limitar el número de caracteres pasando un entero a read(number).
print(type(txt))
print(txt)
f.close()

# Otra forma de obtener todas las líneas como lista es usar splitlines():
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()


# Abrir un archivo para escritura y actualización

# "a" - append - añade al final; crea el archivo si no existe.
with open('./files/reading_file_example.txt','a') as f:
    f.write('Este texto debe añadirse al final')

# "w" - write - sobrescribe el contenido; crea el archivo si no existe.
with open('./files/writing_file_example.txt','w') as f:
    f.write('Este texto será escrito en el nuevo archivo creado')
    
    
# Eliminar archivos
import os
os.remove('./files/example.txt')

# Si el archivo no existe, remove lanzará un error, por lo que es mejor comprobar
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('El archivo no existe')

  

# Archivos con extensión json
# JSON significa JavaScript Object Notation. Es básicamente una representación en cadena de un objeto JavaScript o de un diccionario Python.
# diccionario
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}
# JSON: la forma en cadena del diccionario
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# Usamos triple comillas para que sea multilínea y más legible
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}'''


# Convertir JSON a diccionario
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''
# Convertir la cadena JSON a diccionario
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


# Convertir diccionario a JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# convertir diccionario a cadena JSON
person_json = json.dumps(person, indent=4) # indent puede ser 2, 4, 8; formatea la salida
print(type(person_json))
print(person_json)


# Guardar como archivo JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
    
# Abrir JSON
with open('./files/json_example.json', 'r', encoding='utf-8') as f:
    person = json.load(f)
    print(person)



# Archivos con extensión csv
# Lectura
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w+ crea el archivo si no existe
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Encabezados: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} viene de {row[1]}, {row[2]}. Conoce {row[3]}')
            line_count += 1
    print(f'Procesadas {line_count} líneas.')
    
# Escritura
import csv
with open('./files/csv_example.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # escribir encabezados
    writer.writerow(['name', 'country', 'city', 'skills'])
    # escribir datos
    writer.writerow(['Asabeneh', 'Finland', 'Helsinki', 'JavaScript'])



# Archivos con extensión xlsx
"""
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
"""


# Archivos con extensión xml
# Usamos xml.etree.ElementTree para parsear
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Etiqueta raíz:', root.tag)
print('Atributos:', root.attrib)
for child in root:
    print('Campo: ', child.tag)

# Obtener más detalles
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Etiqueta raíz:', root.tag)
print('Atributos:', root.attrib)
for child in root:
    print('Campo: ', child.tag)
    if child.tag != 'skills':
        print(child.text)
    else:
        for skill in child:
            print(skill.text)



# Ejercicios: Nivel 1
# 1. Escribe una función que reciba un parámetro (nombre de archivo) y cuente el número de palabras del archivo.
def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            texto = f.read()
            palabras = texto.split()
            
            return len(palabras)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return 0
    
print(contar_palabras("./files/reading_file_example.txt"))

# 2. Lee el archivo obama_speech.txt y cuenta las palabras.


# 3. Lee michelle_obama_speech.txt y cuenta las palabras.


# 4. Lee donald_speech.txt y cuenta las palabras.


# 5. Lee melina_trump_speech.txt y cuenta las palabras.


# Ejercicios: Nivel 2
# 1. Extrae todos los archivos Python del directorio del curso: a) Recorre la carpeta 30DaysOfPython, extrae todos los archivos .py y guarda sus nombres en files_list.txt b) Crea un script llamado find_python.py que pueda ejecutarse desde la línea de comandos c) Añade una opción --version para manejar argumentos de línea de comandos