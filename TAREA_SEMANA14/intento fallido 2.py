def calcular_precio_descuento (subtotal , descuento):
    precio_descuento = subtotal - (subtotal * descuento/100)
    return precio_descuento

precio = input("Ingresa los números (enteros o decimales) separados por espacios: ")
lista_numeros = [float(num) for num in precio.split()]
suma_total = sum(lista_numeros)
print(f"Total de su factura es: {suma_total}")

subtotal = suma_total

if precio == "":

    print("Ingrese valores numericos")
else:
    var_temp1 =input("Ingrese el porcentaje de descuento")
    if var_temp1 == "":
        print("ingrese valores numericos")
    else:
        print(precio_descuento)

