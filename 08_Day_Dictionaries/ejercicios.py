# 1. Crea un diccionario vacío llamado dog
dog = {}

# 2. Añade las claves name, color, breed, legs y age al diccionario dog
dog = {"name": "", "color": "", "breed": "", "legs": "", "age": ""}
print(dog)
print(type(dog))

# 3. Crea un diccionario student con las claves first_name, last_name, gender, age, marital status, skills, country, city y address
student = {
    "first_name": "Alejandro",
    "last_name": "Ruidias",
    "gender": "Male",
    "age": 23,
    "marital status": "unmarried",
    "skills": ["skill_1", "skill_2"],
    "country": "Peru",
    "city": "Lima",
    "address": "Calle Ficticia 123"
}

# 4. Obtén la longitud del diccionario student
print(len(student))

# 5. Obtén el valor de skills y comprueba su tipo; debe ser una lista
print(type(student["skills"]))

# 6. Modifica skills añadiendo una o dos habilidades
student["skills"].append("Java")
student["skills"].append("Python")
print(student["skills"])

# 7. Obtén la lista de claves del diccionario
print(student.keys())

# 8. Obtén la lista de valores del diccionario
print(student.values())

# 9. Usa el método items() para convertir el diccionario en una lista de tuplas
print("tuplas: ", student.items())

# 10. Elimina un elemento del diccionario
print(student.pop("marital status"))
del student["address"]

# 11. Elimina uno de los diccionarios
del dog
