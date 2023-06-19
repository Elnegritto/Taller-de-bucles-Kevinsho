# 9.Elabore un algoritmo que permita ingresar n número de temperaturas y escriba la temperatura más alta, la más baja y la temperatura promedio.

n = int(input("Ingrese la cantidad de temperaturas: "))

temperaturas = []
suma_temperaturas = 0
contador = 0

while contador < n:
    temperatura = float(input("Ingrese la temperatura {}: ".format(contador + 1)))
    temperaturas.append(temperatura)
    suma_temperaturas += temperatura
    contador += 1

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
promedio_temperaturas = suma_temperaturas / n

print(f"Temperatura más alta: {temperatura_maxima}")
print(f"Temperatura más baja: {temperatura_minima}")
print(f"Temperatura promedio: {promedio_temperaturas}")
