# 5.crear un programa que permita al usuario ingresar los valores totales de n facturas (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

total_pagar = 0
descuento = 0

while True:
    monto = float(input("Ingrese el monto de la factura (ingrese 0 para finalizar): "))
    
    if monto == 0:
        break

    total_pagar += monto

if total_pagar > 1000:
    descuento = total_pagar * 0.1
    total_pagar -= descuento

print(f"Total a pagar: $ {total_pagar}")
print(f"Descuento aplicado: $ {descuento}")
