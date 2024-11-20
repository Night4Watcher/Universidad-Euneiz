# AL ABRIR EL ARCHIVO CON LA "a" LE ESTAMOS INDICANDO QUE LO ABRA EN MODO ESCRITURA Y LO QUE SE ESCRIBA SE ESCRIBA AL FINAL DEL ARCHIVO
with open("fichero_texto.txt", "a") as fichero:
    fichero.write("\nLinea adicional \n")
    
with open("fichero_texto.txt", "r") as fichero:
    print(fichero.read())