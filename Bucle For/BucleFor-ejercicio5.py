# 5.Hacer un programa que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

numero = int(input("Ingrese un número: "))

suma = 1
contador_impares = 1

for i in range(1, numero+1, 2):
    suma += i
    contador_impares += 1

print(f"La suma de los números impares desde 1 hasta {numero} es: {suma}")
print(f"La cantidad de números impares desde 1 hasta {numero} es: {contador_impares}")
