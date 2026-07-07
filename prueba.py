# Ejercicios: Avanzado
# Usando el archivo countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py), completa lo siguiente:
#   Ordena los países por nombre, capital y población.

import data.countries_data as cd

def order(l: list, filt):
    filt_list = map(lambda country : {
        "name" : country["name"], 
        "capital" : country["capital"], 
        "population" : country["population"]
    }, l)
    
    return sorted(filt_list, key= lambda country : country[filt])

ord_list = order(cd.countries_list, "name")

for country in ord_list:
    print(country)

#   Ordena y obtiene los diez idiomas más usados.
from functools import reduce

def order_lang(l: list):
    lang_list = []
    for country in l:
        for lang in country["languages"]:
            lang_list.append(lang)
            
    def count_lang(acc, language):
        if language not in acc:
            acc[language] = 1
        else:
            acc[language] +=1
        
        return acc
    
    count_dict = reduce(count_lang, lang_list, {})
    most_spok_lang = sorted(count_dict.items(), key= lambda x : x[1], reverse=True)
            
    return most_spok_lang[:10]

print(order_lang(cd.countries_list))

#   Ordena y obtiene los diez países con mayor población.
def order(l: list):
    filt_list = map(lambda country : {"name" : country["name"], "population" : country["population"]}, l)
    
    return sorted(filt_list, key= lambda country : country["population"], reverse=True)

ord_list = order(cd.countries_list)[:10]

for country in ord_list:
    print(country)


