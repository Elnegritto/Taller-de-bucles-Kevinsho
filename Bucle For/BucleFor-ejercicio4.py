# 4. Sumar pares desde 0 hasta el número que indique el usuario

numero = int(input("Ingrese un número: "))

suma = 0
for i in range(0, numero + 1, 2):
    suma += i
print(f"La suma de los números pares desde 0 hasta {numero} es: {suma}")