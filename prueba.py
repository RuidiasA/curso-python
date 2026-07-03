# 6. Convierte la siguiente lista en una lista de cadenas concatenadas:
#       names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#       Salida:
#       ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{item[0]} {item[1]}" for bloque in names for item in bloque]

print(full_names)