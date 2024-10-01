# Archivo de Texto
# Utilizamos el modo "w" para abrir (o crear) el archivo my_notes.txt.
# Si el archivo ya existe, su contenido se sobrescribirá.
with open("my_notes.txt", "w") as file:
    # Escribimos tres líneas de notas personales en el archivo.
    # Cada línea termina con un salto de línea (\n) para asegurarnos de que
    # cada nota aparezca en una línea separada.
    file.write("Nota 1: Levantarse en la mañana.\n")
    file.write("Nota 2: Beber abundante agua.\n")
    file.write("Nota 3: Un poco de ejercicios para iniciar con ánimos.\n")
    file.write("Nota 4: Prerar el desuyuno .\n")
    file.write("Nota 5: Enviar a los niños a la escuela.\n")
    file.write("Nota 5: Realizar las tareas del hogar.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo lectura "r".
# Esto permite acceder al contenido del archivo sin modificarlo.
with open("my_notes.txt", "r") as file:
    # Usamos un bucle for para iterar a través de cada línea del archivo.
    # El método 'readline()' podría ser usado, pero 'for line in file'
    # es más eficiente para leer línea por línea.
    for line in file:
        # La función strip() elimina cualquier espacio en blanco o salto de línea
        # al inicio y al final de cada línea leída, para una presentación más limpia.
        print(line.strip())


