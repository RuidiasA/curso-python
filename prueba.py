# 3. Para la frase "Soy profesor, me gusta motivar y enseñar a las personas." ¿cuántas palabras únicas tiene? Usa split() y conjuntos para obtener las palabras únicas.
frase = "Soy profesor, me gusta motivar y enseñar a las personas."
frase_normalizada = frase.replace(",", "").replace(".", "").lower()

palabras = frase_normalizada.split()
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)
print(len(palabras_unicas))
