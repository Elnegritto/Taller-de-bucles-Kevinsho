# 1. Suma de los n primeros números, solicite al usuario el numero de elementos a suma

n = int(input("Ingrese el número de elementos a sumar: "))

suma = 0

suma = 0

for i in range(1, n+1):
    suma += i

print(f"La suma de los primeros {n} números es: {suma}" )

