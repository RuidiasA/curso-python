# 4. Imprime cada país de la lista countries usando un bucle for.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# 5. Imprime cada nombre de la lista names usando un bucle for.
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# 6. Imprime cada número de la lista numbers usando un bucle for.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce
import data.countries as dc


# 13. Crea una función que devuelva un diccionario donde las claves sean la primera letra de los nombres de país y el valor sea el número de países que comienzan con esa letra.
def count_countries_by_letter(country_list: list):
    def update_letter_counts(letter_counts, country):
        first_letter = country[0]
        
        if first_letter not in letter_counts:
            letter_counts[first_letter] = 1
        else:
            letter_counts[first_letter] += 1
            
        return letter_counts
    
    return reduce(update_letter_counts, country_list, {})

print(count_countries_by_letter(dc.countries))

# 14. Declara una función get_first_ten_countries que devuelva los primeros diez países de la lista countries.js en la carpeta data.


# 15. Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista.
