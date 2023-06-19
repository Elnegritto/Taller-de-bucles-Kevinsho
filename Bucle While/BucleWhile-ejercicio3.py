# 3. Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

n = int(input("Ingrese un número: "))

suma_impares = 0
cantidad_impares = 0
contador = 1

while contador <= n:
    if contador % 2 != 0:
        suma_impares += contador
        cantidad_impares += 1
    contador += 1

print(f"La suma de los números impares desde 1 hasta n es: {suma_impares}")
print(f"La cantidad de números impares es: {cantidad_impares}")

