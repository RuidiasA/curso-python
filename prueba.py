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