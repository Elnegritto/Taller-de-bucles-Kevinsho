# 6.Hacer un programa que pida dos números y muestre todos los números que van desde el primero al segundo, validar que el primer número sea menor que el segundo

numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Escriba el segundo número: "))

if numero1 >= numero2:
    print(f"El primer número debe ser menor que el segundo número.")
else:
    for i in range(numero1, numero2 + 1):
        print(i)
