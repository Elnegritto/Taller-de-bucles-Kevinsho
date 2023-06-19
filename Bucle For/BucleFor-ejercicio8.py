# 8.Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

n = int(input("Ingrese la cantidad de notas: "))

notas = []
for i in range(n):
    nota = float(input("Ingrese la nota {}: ".format(i+1)))
    notas.append(nota)

promedio = sum(notas) / n

print(f"El promedio del estudiante es: {promedio}")


