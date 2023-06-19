# 6.Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

n = int(input("Ingrese la cantidad de notas: "))

suma_notas = 0

for i in range(n):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    suma_notas += nota

promedio = suma_notas / n

print(f"El promedio de las notas es: {promedio}")
