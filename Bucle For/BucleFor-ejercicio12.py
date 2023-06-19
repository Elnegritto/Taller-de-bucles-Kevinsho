# 12.Elaborar un algoritmo que pida las 4 notas de n estudiantes e imprima la nota más alta, la más baja y el promedio.

n = int(input("Ingrese la cantidad de estudiantes: "))

if n <= 0:
    print("Debe ingresar al menos un estudiante.")
else:
    notas_mas_altas = []
    notas_mas_bajas = []
    promedios = []

    for i in range(n):
        print(f"Ingrese las notas del estudiante {i+1}")
        notas = []
        for j in range(4):
            nota = float(input("Ingrese la nota {}: ".format(j+1)))
            notas.append(nota)

        promedio = sum(notas) / len(notas)
        promedios.append(promedio)

        nota_maxima = max(notas)
        notas_mas_altas.append(nota_maxima)

        nota_minima = min(notas)
        notas_mas_bajas.append(nota_minima)

    nota_maxima_global = max(notas_mas_altas)
    nota_minima_global = min(notas_mas_bajas)
    promedio_global = sum(promedios) / len(promedios)

    print(f"Nota más alta: {nota_maxima_global}")
    print(f"Nota más baja: {nota_minima_global}")
    print(f"Promedio general: {promedio_global}")
