# 1. Une las cadenas 'Thirty', 'Days', 'Of', 'Python' en 'Thirty Days Of Python'.
cadenas = ["Thirty", "Days", "Of", "Python"]
print(" ".join(cadenas))

# 2. Une las cadenas 'Coding', 'For', 'All' en 'Coding For All'.
cad_1 = "Coding"
cad_2 = "For"
cad_3 = "All"
print(f"{cad_1} {cad_2} {cad_3}")

# 3. Declara la variable company y asígnale el valor inicial "Coding For All".
company = "Coding For All"

# 4. Imprime la variable company usando print().
print(company)

# 5. Usa len() y print() para mostrar la longitud de la cadena company.
print(len(company))

# 6. Usa el método upper() para convertir todos los caracteres a mayúsculas.
print(company.upper())

# 7. Usa el método lower() para convertir todos los caracteres a minúsculas.
print(company.lower())

# 8. Aplica capitalize(), title() y swapcase() sobre la cadena 'Coding For All'.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Extrae mediante slicing la primera palabra de 'Coding For All'.
print(company[0:6])

# 10. Usa index, find u otros métodos para comprobar si la cadena 'Coding For All' contiene la palabra 'Coding'.
print(company.index("Coding"))
print(company.find("Coding"))
print(company.index("Coding") != -1)
print("Coding" in company)

# 11. Reemplaza la palabra 'Coding' por 'Python' en 'Coding For All'.
print(company.replace("Coding", "Python"))

# 12. Reemplaza 'Python for Everyone' por 'Python for All' (usa replace() u otro método).
sentence = "Python for Everyone"
print(sentence.replace("Everyone", "All"))

# 13. Separa la cadena 'Coding For All' usando espacios como separador.
print(company.split())

# 14. Divide la cadena 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' por las comas.
cadena = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(cadena.split(", "))

# 15. ¿Qué carácter está en el índice 0 de 'Coding For All'?
print(company[0])

# 16. ¿Cuál es el índice del último carácter de 'Coding For All'?
print(company[-1])

# 17. ¿Qué carácter está en el índice 10 de 'Coding For All'?
print(company[10])

# 18. Crea una sigla (acrónimo) a partir de 'Python For Everyone'.
sent_words = sentence.split()
print(sent_words[0][0] + sent_words[1][0] + sent_words[2][0])

# 19. Crea una sigla a partir de 'Coding For All'.
comp_words = company.split()
print(comp_words[0][0] + comp_words[1][0] + comp_words[2][0])

# 20. Usando index, determina la primera aparición de la letra 'C' en 'Coding For All'.
print(company.index("C"))

# 21. Usando index, determina la primera aparición de la letra 'F' en 'Coding For All'.
print(company.index("F"))

# 22. Usa rfind para determinar la última aparición de 'l' en 'Coding For All People'.
print("Coding For All People".rfind("l"))

# 23. Usa index o find para encontrar la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'
sentence_2 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_2.index("because"))

# 24. Usa rindex para encontrar la última aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.
print(sentence_2.rindex("because"))

# 25. Elimina la frase 'because because because' de: 'You cannot end a sentence with because because because is a conjunction'.
print(sentence_2.replace("because because because ", ""))

# 26. Encuentra la primera aparición de la palabra 'because' en: 'You cannot end a sentence with because because because is a conjunction'.
print(sentence_2.find("because"))

# 27. Elimina la frase 'because because because' de la oración anterior.
print(sentence_2[0:31] + sentence_2[55:])

# 28. ¿La cadena 'Coding For All' empieza con la subcadena 'Coding'?
print(company.startswith("Coding"))

# 29. ¿La cadena 'Coding For All' termina con la subcadena 'coding'?
print(company.endswith("coding"))

# 30. Elimina los espacios en blanco a la izquierda y derecha de la cadena '   Coding For All      '.
print('   Coding For All      '.strip())

# 31. Usando isidentifier(), ¿cuál de las siguientes devuelve True?
#     30DaysOfPython
#     thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. Dada la lista ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'], únela en una cadena separada por espacios.
lista = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(lista))

# 33. Usa la secuencia de escape de nueva línea para separar las siguientes oraciones:
#     I am enjoying this challenge.
#     I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Usa la secuencia de tabulación para mostrar:
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki".expandtabs(10))

# 35. Usa un método de formateo de cadenas para imprimir:
#     radius = 10
#     area = 3.14 * radius ** 2
#     The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
# Opción 1: Con f-string
print(
    f"The area of a circle with radius {radius} is {area:.0f} meters square.")
# Opción 2: Con el operador %
print("The area of a circle with radius %d is %.0f meters square." % (radius, area))

# 36. Usa un método de formateo de cadenas para imprimir:
#     8 + 6 = 14
#     8 - 6 = 2
#     8 * 6 = 48
#     8 / 6 = 1.33
#     8 % 6 = 2
#     8 // 6 = 1
#     8 ** 6 = 262144
num_1 = 8
num_2 = 6
print(f"""
      {num_1} + {num_2} = {num_1 + num_2}
      {num_1} - {num_2} = {num_1 - num_2}
      {num_1} * {num_2} = {num_1 * num_2}
      {num_1} / {num_2} = {(num_1 / num_2):.2f}
      {num_1} % {num_2} = {num_1 % num_2}
      {num_1} // {num_2} = {num_1 // num_2}
      {num_1} ** {num_2} = {num_1 ** num_2}
      """)

print(f"{num_1} + {num_2} = {num_1 + num_2}")
print(f"{num_1} - {num_2} = {num_1 - num_2}")
print(f"{num_1} * {num_2} = {num_1 * num_2}")
print(f"{num_1} / {num_2} = {(num_1 / num_2):.2f}")
print(f"{num_1} % {num_2} = {num_1 % num_2}")
print(f"{num_1} // {num_2} = {num_1 // num_2}")
print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
