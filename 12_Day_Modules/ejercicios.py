# Ejercicios: Nivel 1
# 1. Escribe una función que genere un random_user_id de seis caracteres/dígitos.
#       print(random_user_id());
#         '1ee33d'
import random as rd
import string as st

def random_user_id():
    poss_char = st.ascii_lowercase + st.digits
    id_6 = "".join(rd.choices(poss_char, k=6))
    return id_6

print(random_user_id())

# 2. Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. 
#    No acepta argumentos, pero pide dos entradas: una es la cantidad de caracteres por ID y la otra es cuántos IDs generar.
#       print(user_id_gen_by_user()) # entrada del usuario: 5 5
#       salida:
#       kcsy2
#       SMFYb
#       bWmeq
#       ZXOYh
#       2Rgxf
#       print(user_id_gen_by_user()) # 16 5
#       1GCSgPLMaBAVQZ26
#       YD7eFwNQKNs7qXaT
#       ycArC5yrRupyG00S
#       UbGxOFI7UXSWAyKN
#       dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    cant_char = int(input("Ingrese la cantidad de caracteres por ID: "))
    num_ids = int(input("Ingrese la cantidad de IDs a generar: "))
    poss_char = st.ascii_letters + st.digits
    for _ in range(num_ids):
        id_gen = "".join(rd.choices(poss_char, k=cant_char))
        print(id_gen)

user_id_gen_by_user()

# 3. Escribe una función llamada rgb_color_gen. Debe generar un color RGB (cada valor en el rango 0-255).
#       print(rgb_color_gen())
#       rgb(125,244,255) - la salida debe estar en este formato
def rgb_color_gen():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)

    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())


# Ejercicios: Nivel 2
# 1. Escribe una función list_of_hexa_colors que devuelva una lista con cualquier cantidad de colores hexadecimales (seis dígitos hexadecimales después de #; el sistema hex usa 0-9 y a-f).
def list_of_hexa_colors(n):
    poss_char = st.ascii_lowercase[:6] + st.digits  # string tiene una variable nativa: hexdigits que facilita esto
    hex_list = []
    for _ in range(n):
        hex_gen = "#" + "".join(rd.choices(poss_char, k=6))
        hex_list.append(hex_gen)
    
    return hex_list

print(list_of_hexa_colors(6))

# 2. Escribe una función list_of_rgb_colors que devuelva una lista con cualquier cantidad de colores RGB.
def list_of_rgb_colors(n):
    rgb_list=[]
    for _ in range(n):
        r = rd.randint(0,255)
        g = rd.randint(0,255)
        b = rd.randint(0,255)
        rgb = f"rgb({r}, {g}, {b})"
        rgb_list.append(rgb)
        
    return rgb_list

print(list_of_rgb_colors(2))

# 3. Escribe una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o RGB.
#       generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#       generate_colors('hexa', 1) # ['#b334ef']
#       generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#       generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(t, c):
    colors_list = []
    
    if t == "hexa":
        poss_hex = st.digits + st.ascii_lowercase[:6]
        for _ in range(c):
            hex_color = "#" + "".join(rd.choices(poss_hex, k=6))
            colors_list.append(hex_color)        

        return colors_list
    
    elif t == "rgb":
        for _ in range(c):
            r = rd.randint(0, 255)
            g = rd.randint(0, 255)
            b = rd.randint(0, 255)
            rgb = f"rgb({r}, {g}, {b})"
            colors_list.append(rgb)
            
        return colors_list
    
    return "Error: Tipo de color no soportado. Usa 'hexa' o 'rgb'."

print(generate_colors("hexa", 5))
print(generate_colors("rgb", 3))

# Ejercicios: Nivel 3
# 1. Llama a tu función shuffle_list, que recibe una lista y devuelve la lista mezclada.
def shuffle_list(l: list):
    unord_list = l.copy()
    n = len(l)
    
    for i in range(n - 1, 0, -1):
        rand_ind = rd.randint(0, i)
        unord_list[i], unord_list[rand_ind] = unord_list[rand_ind], unord_list[i]
        
    return unord_list

print(shuffle_list(["1", "a", "2", "b", "3", "c"]))

# 2. Escribe una función que devuelva una lista de siete números aleatorios únicos en el rango 0-9.
def uniq_rand_numb():
    uniq_rand_numb_list = []
    while len(uniq_rand_numb_list) < 7:
        dig = rd.randint(0,9)
        if dig not in uniq_rand_numb_list:
            uniq_rand_numb_list.append(dig)
        
    return uniq_rand_numb_list
    # return rd.sample(range(10), 7) <-- Version en una sola linea, range(10) te da los números del 0 al 9, ademas podemos usar set() con .add ya que set() ignora duplicados

print(uniq_rand_numb())