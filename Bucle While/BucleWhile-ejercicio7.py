# 7.Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

suma = 0

while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))

    if numero == 0:
        break

    suma += numero

print(f"La sumatoria de los números ingresados es: {suma}")
