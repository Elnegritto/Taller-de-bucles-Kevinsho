# 11.Elabore un algoritmo que pregunte cuántas temperaturas se van a introducir, pida esas temperaturas, y escriba la temperatura más alta, la más baja y la temperatura promedio.

cantidad_temperaturas = int(input("Ingrese una cantidad de temperaturas a digitar: "))

if cantidad_temperaturas <= 0:
    print("Debes ingresar al menos una temperatura brut@.")
else:
    temperaturas = []
    for i in range(cantidad_temperaturas):
        temperatura = float(input("Ingrese la temperatura {}: ".format(i+1)))
        temperaturas.append(temperatura)

    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_promedio = sum(temperaturas) / cantidad_temperaturas

    print(f"Temperatura más alta: {temperatura_maxima}")
    print(f"Temperatura más baja: {temperatura_minima}")
    print(f"Temperatura promedio: {temperatura_promedio}")

