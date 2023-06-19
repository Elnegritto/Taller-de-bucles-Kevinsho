# 2.  Digite un número, si el numero supera a 10, multiplique los 10 primeros 

numero = int(input("Ingrese un número: "))

if numero > 10:
     resultado = 1
     for i in range(1, 11):
        resultado *= i
    
     print(f"El resultado de multiplicar los 10 primeros números es: {resultado}")

