import data.countries as c
import data.countries_data as cd

# 3. Ve a la carpeta data y usa el archivo countries-data.py.
# 1. Ve a la carpeta data y usa el archivo countries.py. Itera los países y extrae aquellos que contienen la cadena land.
for country in c.countries:
    if "land" in country.lower():
        print(country)

#     ii. ¿Cuál es el idioma usado por más países?
lang = list()
for country in cd.countries_list:
    lang_list = country["languages"]
    for i in lang_list:
        lang.append(i)
# print(lang)

count_lang = dict()
for l in lang:
    if l not in count_lang:
        count_lang[l] = 1
    else:
        count_lang[l] += 1
# print(count_lang)

max_lang = ""
max_qnt = 0
for i, q in count_lang.items():
    # print(i, q)
    if q > max_qnt:
        max_lang = i
        max_qnt = q

print(max_lang, max_qnt)

#    iii. Encuentra los diez países con mayor población.
most_pop_countries = []
for p in cd.countries_list:
    if len(most_pop_countries) < 10:
        most_pop_countries.append((p["population"], p["name"]))
        most_pop_countries.sort(reverse=True)
    elif p["population"] > most_pop_countries[-1][0]:
        most_pop_countries[-1] = (p["population"], p["name"])
        most_pop_countries.sort(reverse=True)

for rank, (pop, name) in enumerate(most_pop_countries, 1):
    print(f"{rank}. {name} - Población: {pop:,}")
