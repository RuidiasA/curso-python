import random as rd
import string as st

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