#Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).

#La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.

#La función debe devolver el monto del descuento calculado

def calcular_descuento (monto_total,porcentaje_descuento=20):
    descuento = monto_total * porcentaje_descuento/100
    return descuento

#calculo = calcular_descuento(1000, 10)
#print(calculo)
#calculo = calcular_descuento(1000)
#print(calculo)
items_compra = []
items_compra.append(calcular_descuento(523,15))
items_compra.append(calcular_descuento(252,12))
items_compra.append(calcular_descuento(135,10))
items_compra.append(calcular_descuento(695,9))
items_compra.append(calcular_descuento(223,18))
print(items_compra)
acumulador = 0
for i in range(len(items_compra)):
    acumulador = acumulador +items_compra[i]
print(acumulador)



