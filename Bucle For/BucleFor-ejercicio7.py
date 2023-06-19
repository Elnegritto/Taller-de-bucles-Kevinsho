# 7.Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10.

tabla_de_multiplicacion = int(input("Ingrese el número de la tabla de multiplicacion que desea ver: "))

print(f"Tabla de multiplicar del {tabla_de_multiplicacion}")
for i in range(11):
    resultado = tabla_de_multiplicacion * i
    print(tabla_de_multiplicacion, "x", i, "=", resultado)
