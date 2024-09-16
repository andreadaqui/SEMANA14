#Creamos una funciòn que nos calcule el valor menos el descuento
def calcular_precio_descuento (precio, descuento):
    precio_descuento = precio - (precio * descuento/100)
#el valor que nos retorna es el precio de descuento
    return precio_descuento
#Creamos una variable donde se guarda el valor
total = 0
#Creamos la variable donde se ingresa el valor del producto
var_temp = input("Ingrese el precio del producto")
#Si el valor del producto esta vacio
if var_temp == "":
#Le muestra el mensaje que debe ingresar un valor numèrico
    print("Ingrese valores numericos")
#Caso contrario ingresar el porcentaje de descuento
else:
    var_temp1 =input("Ingrese el porcentaje de descuento")
    if var_temp1 == "":
        print("ingrese valores numericos") #mensaje que ingrese un valor numerico
#Caso contrario llamar a la funciòn
    else:
        total = calcular_precio_descuento(float(var_temp), float(var_temp1))
#Imprimir el valor total
print(total)

