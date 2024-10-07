import os

# BLOQUE ELIMINADOR DE CARPETAS
def eliminador_carpetas():
    nombre_carpeta = input("¿Que carpeta quieres eliminar? ")
    lista_carpetas = os.listdir(f"{os.path.expanduser('~')}/Desktop")
    os.chdir(f"{os.path.expanduser('~')}/Desktop")
    contador_archivos = 0
    for item in lista_carpetas:
        nombre_carpeta = f"{nombre_carpeta}{contador_archivos}"
        if item == nombre_carpeta:
            os.rmdir(f"{os.path.expanduser('~')}/Desktop{nombre_carpeta}")
        contador_archivos += 1

# BLOQUE DE CREADOR DE CARPETAS INDIVIDUALES
def creador_carpeta_individual():
    nombre_carpeta = input("Dame un nombre para la carpeta: ")
    os.chdir(f"{os.path.expanduser('~')}/Desktop")
    os.mkdir(nombre_carpeta)

# BLOQUE DE CREADOR DE CARPETAS CON AÑADIDO NUMERICO
def creador_carpetas_bucle(n_carpetas):
    nombre_carpeta = input("Dame un nombre para las carpetas: ")
    cantidad_carpetas = n_carpetas
    carpetas_creadas = 0
    os.chdir(f"{os.path.expanduser('~')}/Desktop")
    while carpetas_creadas < cantidad_carpetas:
        os.mkdir(f"{nombre_carpeta}{carpetas_creadas + 1}")
        carpetas_creadas += 1

# BLOQUE PRINCIPAL DEL PROGRAMA
def main():
    os.system("clear")
    print("Bienvenido a tu creador de carpetas personal.")
    input("Pulsa enter para continuar...")
    # BORRADO GENERAL DE LO QUE ESTA MOSTRANDO EL TERMINAL
    os.system("clear")
    seleccion_uso = input("¿Quieres crear o eliminar carpetas del escritorio? ")
    if seleccion_uso.upper() == "CREAR":    
        cantidad_carpetas_crear = int(input("¿Cuantas carpetas quieres crear? "))
        if cantidad_carpetas_crear < 2:
            print("De acuerdo, vamos a crear una unica carpeta")
            creador_carpeta_individual()
        elif cantidad_carpetas_crear >= 2:
            print(f"Vamos a crear {cantidad_carpetas_crear} o mas carpetas")
            creador_carpetas_bucle(cantidad_carpetas_crear)
    elif seleccion_uso.upper() == "ELIMINAR":
        cantidad_carpetas_eliminar = int(input("¿Cuantas carpetas quieres eliminar? "))
        if cantidad_carpetas_eliminar < 2:
            print("De acuerdo, vamos a eliminar unicamente una carpeta")
            # EJECUCION DEL PROGRAMA DE ELIMINACION DE UNA UNICA CARPETA
        elif cantidad_carpetas_eliminar >= 2:
            print(f"Vamos a eliminar {cantidad_carpetas_eliminar} carpetas.")
            eliminador_carpetas()
            # EJECUCION DEL PROGRAMA DE ELIMINACION DE VARIAS CARPETAS

main()