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
