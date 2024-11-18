palabra_buscar = input("¿Que palabra quieres que busquemos en el fichero? ")
resultado = 0

with open("texto.txt", "r") as fichero:
    num_linea = 1
    for linea in fichero:
        linea = linea.strip()
        if linea.find(palabra_buscar) != -1:
            resultado = 1
            print(f"Hola hemos encontrado la palabra {palabra_buscar} en la linea {num_linea}")
        num_linea += 1 
    if resultado == 0:
        print(f"No se ha encontrado la palabra {palabra_buscar}")