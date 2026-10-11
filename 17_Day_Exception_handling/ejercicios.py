# Sintaxis TRY / EXCEPT
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - year_born
    print(f'Eres {name}. Tu edad es {age}.')
except:
    print('Ocurrió un error')

# Tipos de error
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - year_born
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print('Se produjo un error de tipo (TypeError)')
except ValueError:
    print('Se produjo un ValueError')
except ZeroDivisionError:
    print('Se produjo una división por cero (ZeroDivisionError)')

# 
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print('Se produjo un error de tipo (TypeError)')
except ValueError:
    print('Se produjo un ValueError')
except ZeroDivisionError:
    print('Se produjo una división por cero (ZeroDivisionError)')
else:
    print('Este bloque se ejecuta normalmente después de try')
finally:
    print('Este bloque siempre se ejecuta.')
    
# Simplificado
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except Exception as e:
    print(e)
    

# DESEMPAQUETADO (Operador *)
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# Desempaquetando listas (*lst)
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15

# Desempaquetando rangos (range(*args))
numbers = range(2, 7)  # llamada normal con parámetros separados
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # llamada usando los parámetros desempaquetados desde la lista
print(list(numbers))      # [2, 3, 4, 5, 6]

# Desempaquetando asignaciones
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# Desempaquetando diccionarios (**dct)
def unpacking_person_info(name, country, city, age):
    return f'{name} vive en {city}, {country}. Tiene {age} años.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh vive en Helsinki, Finland. Tiene 250 años.


# EMPAQUETADO 

# Empaquetando listas
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# Empaquetando diccionarios
def packing_person_info(**kwargs):
    # comprobar el tipo de kwargs: es un dict
    # print(type(kwargs))
    # imprimir los pares clave-valor
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


# Expandir listas
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]


# Enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)
    
for index, i in enumerate(countries):
    print('hola')
    if i == 'Finland':
        print(f'El país {i} está en el índice {index}')
        

# Combinando listas con ZIP
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


# Ejercicios: Día 17

# 1. Crea en countries.py funciones que usen los datos de countries_data.py:
#    una función para encontrar los 10 idiomas más usados
import data.countries_data as cd

def most_used_langs(n):
    count_lang = {}
    
    for country in cd.countries_list:
        try:
            lang_country = country["languages"]
            for lang in lang_country:
                if lang not in count_lang:
                    count_lang[lang] = 1
            else:
                count_lang[lang] += 1
        except KeyError:
            continue
        
    sorted_langs = sorted(count_lang.items(), key=lambda item: item[1], reverse=True)
    top_langs = sorted_langs[:n]
        
    return top_langs
    
print(most_used_langs(10))

#    una función para encontrar los 10 países más poblados
def most_pop_countries(n):
    country_name_lst = []
    country_population_lst = []
    most_pop_countries_list = []
    
    for country in cd.countries_list:
        try:
            country_name_lst.append(country["name"])
            country_population_lst.append(country["population"])
        except KeyError:
            continue
        
    for name, population in zip(country_name_lst, country_population_lst):
                most_pop_countries_list.append({"Pais":name, "Poblacion":population})
                
    sorted_pop = sorted(most_pop_countries_list, key= lambda item: item["Poblacion"] , reverse=True)
    top_pop = sorted_pop[:n]
    
    return top_pop
        
print(most_pop_countries(10))


# Version Optimizada
def most_pop_countries_opt(cant):
    countries_data = []
    
    for country in cd.countries_list:
        try:
            countries_data.append({
                "Pais": country["name"],
                "Poblacion": country["population"]
            })
        except KeyError:
            continue
    
    sorted_pop = sorted(countries_data, key=lambda item: item["Poblacion"], reverse=True)
    top_pop = sorted_pop[:cant]
    
    return top_pop

print(most_pop_countries_opt(10))