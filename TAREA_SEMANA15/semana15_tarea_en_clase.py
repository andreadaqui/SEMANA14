#En primer lugar creamos una variable para guardar los datos
libros=[]

#creamos un ciclo para realizar la captura de los datos
while True:
    #Aqui vamos a capturar los datos
    lib_nombre = input("Ingrese el nombre del libro:")
    lib_categoria = input("Ingrese la categoria del libro:")
    lib_año_publicacion = input("Ingrese el año de publicaciòn:")
    lib_hoja = input("Ingrese el nùmero de hojas:")
    #Guardamos estos datos en un diccionario denominado
    libro = {
        "nombre":lib_nombre,
        "categoria":lib_categoria,
        "año_pubicacion":lib_año_publicacion,
        "numero_hojas":lib_hoja

    }
    # Añadimos el libro a la lista de libros
    libros.append(libro)
    #Preguntamos al usuario si quiere ingresar otro libro caso contrario salir
    continuar = input("¿Desea ingresar otro libro si/no?:")
    if continuar.lower()!= "si":
        break

    #Imprimimos el listado de los datos ingresados
    print("\nListado de libros:")
    for libro in libros:
       print(libro)

