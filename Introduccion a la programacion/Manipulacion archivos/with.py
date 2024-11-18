with open("fichero_texto.txt", "w") as fichero:
    # MEDIANTE EL .write() ESCRIBIREMOS EN EL ARCHIVO LO QUE INTRODUZCAMOS ENTRE COMILLAS EN EL PARENTESIS.
    fichero.write("Hola mundo")
    fichero.write("\n")
    fichero.write("Nuevo texto")
    # MEDIANTE EL .close() CERRAMOS EL ARCHIVO
    fichero.close()