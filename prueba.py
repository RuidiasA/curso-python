# Ejercicios: Nivel 1
# 2. Lee el archivo obama_speech.txt y cuenta las palabras.

def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            texto = f.read()
            palabras = texto.split()
            
            return len(palabras)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}.")
        return 0
    
print(contar_palabras("./data/melina_trump_speech.txt"))