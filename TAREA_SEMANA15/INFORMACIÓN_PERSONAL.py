# Creamos un diccionario que contenga información ficticia
informacion_personal = {
    "nombre": "Andrea Daqui",
    "edad": 37,
    "ciudad": "Ibarra",
    "profesion": "Comerciante",
    "pasatiempo": "Leer"
   }

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"]="Riobamba"

# Agregar una nueva clave-valor que represente la "profesion"
informacion_personal["profesion"] = "Ama de casa"


# Verificar si la clave "telefono" existe, y si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989345033"

# Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir el diccionario resultante
print("Diccionario final:")
print(informacion_personal)


