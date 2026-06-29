# 5. Accede al archivo de datos countries-data.py.
import data.countries_data as cd
#     Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
def the_most_spoken_languages(n):
    lang_list = []
    for country in cd.countries_list:
        lang_country = country["languages"]
        for lang in lang_country:
            lang_list.append(lang)
    
    count_lang = dict()
    for lang in lang_list:
        if lang not in count_lang:
            count_lang[lang] = 1
        else:
            count_lang[lang] += 1
    
    ord_lang = sorted(count_lang.values(), reverse=True)[:n]
    count_lang_copy = count_lang.copy()
    
    most_spok_lang = dict()
    for cant in ord_lang:
        for key, value in list(count_lang_copy.items()):
            if value == cant:
                most_spok_lang[key] = cant
                del count_lang_copy[key]
                break
    
    return most_spok_lang

print(the_most_spoken_languages(20))

#     Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.