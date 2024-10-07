import os

# BLOQUE DE CREADOR DE CARPETAS INDIVIDUALES
def creador_carpeta_individual():
    nombre_carpeta = input("Dame un nombre para la carpeta: ")
    os.mkdir(nombre_carpeta)

# BLOQUE DE CREADOR DE CARPETAS CON AÑADIDO NUMERICO
def creador_carpetas_bucle():
    nombre_carpeta = input("Dame un nombre para las carpetas: ")
    cantidad_carpetas = int(input("¿Cuantas carpetas quieres crear? "))
    carpetas_creadas = 0
    while carpetas_creadas < cantidad_carpetas:
        os.mkdir(f"{nombre_carpeta}{carpetas_creadas}")
        carpetas_creadas += 1

# BLOQUE PRINCIPAL DEL PROGRAMA
def main():
    print("Bienvenido a tu creador de carpetas personal.")
    input("Pulsa enter para continuar...")
    # BORRADO GENERAL DE LO QUE ESTA MOSTRANDO EL TERMINAL
    os.system("clear")
    cantidad_carpetas = int(input("¿Cuantas carpetas quieres crear? "))
    if cantidad_carpetas < 2:
        print("De acuerdo, vamos a crear una unica carpeta")
        creador_carpeta_individual()
    elif cantidad_carpetas >= 2:
        print("Vamos a crear 2 o mas carpetas")
        creador_carpetas_bucle()

main()