# 2. Llama a tu función factorial que acepte un entero y devuelva su factorial.
def factorial(n):
    f = 1
    for num in range(1, n + 1):
        f *= num
    return f
print(factorial(5))