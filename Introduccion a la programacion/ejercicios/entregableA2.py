import random

# VARIABLES GENERALES PARA IDENTIFICACION Y USO DE CARACTERES
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caracteres_especiales = ['!', '@', '#', '$', '%']

def generador_contraseñas(longitud, mayusculas_main, especiales_main, digitos_main):
    """
    Esta funcion esta encargada de la generacion de contraseñas en funcion a los parametros introducidos previamente en la funcion principal del programa
    
    Keyword arguments:
    longitud -- Longitud de la contraseña establecida por el usuario en la funcion principal del programa.
    mayusculas_main -- Cantidad de mayusculas que tienen que haber en la contraseña introducidos previamente por el usuario en la funcion principal del programa.
    especiales_main -- Cantidad de caracteres especiales que tienen que haber en la contraseña introducidos previamente por el usuario en la funcion principal del programa.
    digitos_main -- Cantidad de digitos que tiene que haber en la contraseña introducidos previamente por el usuario en la funcion principal del programa.
    contraseña -- Esta variable es la contraseña final que se habra generado.
    cantidad_caracteres -- Esta variable es la que se encarga de contabilizar la cantidad de caracteres de la contraseña que esta siendo generada por la funcion.
    cantidad_mayusculas -- Esta variable es la que se encarga de contabilizar la cantidad de mayusculas de la contraseña que esta siendo generada por la funcion.
    cantidad_especiales -- Esta variable es la que se encarga de contabilizar la cantidad de caracteres especiales de la contraseña que esta siendo generada por la funcion.
    cantidad_digitos -- Esta variable es la que se encarga de contabilizar la cantidad de digitos de la contraseña que esta siendo generada por la funcion.
    Return: Devuelve una contraseña que cumpla con todos los parametros introducidos por el usuario en la funcion principal del programa.
    """
    
    # VARIABLES LOCALES DE LA FUNCION
    contraseña = ""
    cantidad_caracteres = 0
    cantidad_mayusculas = 0
    cantidad_especiales = 0
    cantidad_digitos  = 0
    while cantidad_caracteres < longitud or cantidad_mayusculas < mayusculas_main or cantidad_especiales < especiales_main or cantidad_digitos < digitos_main:
        # OBTENCION DEL CARACTER QUE SE LE VA A INTRODUCIR A LA CONTRASEÑA
        caracter_introducir = random.randint(0, 2)
        # LETRA A INTRODUCIR A LA CONTRASEÑA
        if caracter_introducir == 0:
            # OBTENCION DE SI LA LETRA A INTRODUCIR SERA MAYUSCULA O MINUSCULA
            tipo_letra = random.randint(0,1)
            # AÑADIR LA MINUSCULA A LA CONTRASEÑA
            if tipo_letra == 0:
                letra = random.choice(minusculas)
                contraseña = contraseña + letra
            # AÑADIR LA MAYUSCULA A LA CONTRASEÑA
            elif tipo_letra == 1 and (cantidad_mayusculas < mayusculas_main):
                letra = random.choice(mayusculas)
                contraseña = contraseña + letra
                cantidad_mayusculas += 1
            cantidad_caracteres += 1
        # CARACTER ESPECIAL A INTRODUCIR EN LA CONTRASEÑA
        elif caracter_introducir == 1 and (cantidad_especiales < especiales_main):
            # OBTENCION DEL CARACTER ESPECIAL A INTRODUCIR A LA CONTRASEÑA
            caracter_especial = random.choice(caracteres_especiales)
            contraseña = contraseña + caracter_especial
            cantidad_especiales += 1
            cantidad_caracteres += 1
        # DIGITO A INTRODUCIR EN LA CONTRASEÑA
        elif caracter_introducir == 2 and (cantidad_digitos < digitos_main):
            digito = random.choice(digitos)
            contraseña = contraseña + digito
            cantidad_digitos += 1
            cantidad_caracteres += 1
    return contraseña

def guardad_contraseña(fichero_usuario, contraseña_generada):
    """
    Esta funcion esta encargada de guardar la ultima contraseña que haya sido generada mediante el programa.
    
    Keyword arguments:
    fichero_usuario -- Nombre introducido por el usuario para el fichero en el cual se almacenara la contraseña.
    contraseña_generada -- Contraseña que ha sido generada por el programa y que se va a almacenar en el fichero
    Return: La funcion no devuelve nada, simplemente genera un archivo txt
    """
    with open(f"{fichero_usuario}.txt", "a") as fichero:
        fichero.write(f"{contraseña_generada}")

def recuperar_contraseña(fichero_buscar):
    """
    Esta funcion se encarga de buscar la contraseña que haya en un fichero donde el nombre del fichero haya sido introducido previamente por el usuario.
    
    Keyword arguments:
    fichero_buscar -- Nombre del fichero en el que hay que buscar la contraseña introducido previamente por el usuario en la funcion principal del programa
    Return: La funcion devuelve la contraseña que ha encontrado en el fichero
    """
    with open(f"{fichero_buscar}.txt", "r") as fichero:
        contraseña_archivo = fichero.read()
    return contraseña_archivo

def buscar_contraseña(contraseña_buscar, fichero_buscar):
    """
    Esta funcion se encarga de buscar la contraseña introducida por el usuario en la funcion principal del programa en el fichero que se haya introducido previamente por el usuario en la funcion principal del programa.
    
    Keyword arguments:
    contraseña_buscar -- Esta es la contraseña que tiene que buscar la funcion en el fichero
    fichero_buscar -- Este es el nombre del fichero en el cual la funcion tiene que buscar la contraseña
    linea_revision --
    busqueda -- 
    Return: Devuelve si se ha encontrado la contraseña y en que linea se ha encontrado o si no se ha encontrado
    """
    
    linea_revision = 0
    with open(f"{fichero_buscar}.txt", "r") as fichero:
        for lineas in fichero:
            linea_revision += 1
            if lineas.find(contraseña_buscar) != (-1):
                return f"La contraseña se ha encontrado en la linea {linea_revision}"
    return f"No se ha encontrado la contraseña en el fichero {fichero_buscar}"
def main():
    contraseña = None
    seleccion_usuario = int(input(
    """
    Bienvenido a tu gestor de contraseñas, que desear realizar?
    1. Generar contraseña
    2. Guardar contraseña en un fichero
    3. Recuperar contraseña de fichero
    4. Buscar contraseña en fichero
    5. Salir
    """
    ))
    while seleccion_usuario != 5:
        match seleccion_usuario:
            case 1:
                print("De acuerdo, vamos a generar la contraseña, antes de nada necesitamos los siguientes datos:")
                # OBTENCION DE LA CANTIDAD DE CARACTERES QUE TENGA QUE TENER LA CONTRASEÑA
                longitud = int(input("¿Cuantos caracteres quieres que tenga la contraseña? "))
                # ASEGURAR QUE LA CONTRASEÑA TENGA UNA LONGITUD MINIMA
                while longitud < 8:
                    print("La contraseña no puede tener menos de 8 caracteres.")
                    longitud = int(input("¿Cuantos caracteres quieres que tenga la contraseña? "))
                # OBTENCION DE LA CANTIDAD DE MAYUSCULAS QUE TENGA QUE TENER LA CONTRASEÑA
                cantidad_mayusculas = int(input("¿Cuantas mayusculas quieres que tenga la contraseña? "))
                # ASEGURAR QUE LA CONTRASEÑA TENGA UNA CANTIDAD DE MAYUSCULAS MINIMA
                while cantidad_mayusculas < 1:
                    print("La contraseña tiene que tener minimo 1 mayuscula.")
                    cantidad_mayusculas = int(input("¿Cuantas mayusculas quieres que tenga la contraseña? "))
                # OBTENCION DE LA CANTIDAD DE CARACTERES ESPECIALES QUE TENGA QUE TENER LA CONTRASEÑA
                cantidad_especiales = int(input("¿Cuantos caracteres especiales quieres que tenga la contraseña? "))
                # ASEGURAR QUE LA CONTRASEÑA TENGA UNA CANTIDAD DE CARACTERES ESPECIALES MINIMA
                while cantidad_especiales < 1:
                    print("La contraseña tiene que tener minimo 1 carater especial.")
                    cantidad_especiales = int(input("¿Cuantos caracteres especiales quieres que tenga la contraseña? "))
                # OBTENCION DE LA CANTIDAD DE DIGITOS QUE TENGA QUE TENER LA CONTRASEÑA
                cantidad_digitos = int(input("¿Cuantos digitos quieres que tenga la contraseña? "))
                # ASEGURAR QUE LA CONTRASEÑA TENGA UNA CANTIDAD DE DIGITOS MINIIMA
                while cantidad_digitos < 1:
                    print("La contraseña tiene que tener minimo 1 digito")
                    cantidad_digitos = int(input("¿Cuantos digitos quieres que tenga la contraseña? "))
                # LLAMADO A LA FUNCION DE GENERADOR DE CONTRASEÑAS CON LOS PARAMETROS INTRODUCIDOS POR EL USUARIO
                contraseña = generador_contraseñas(longitud, cantidad_mayusculas, cantidad_especiales, cantidad_digitos)
                # MOSTRARLE AL USUARIO EN PANTALLA LA CONTRASEÑA GENERADA
                print(f"La contraseña generada ha sido {contraseña}")
            case 2:
                # COMPROBACION DE SI SE HA GENERADO ALGUNA CONTRASEÑA O NO
                if contraseña != None:
                    print("De acuerdo, vamos a guardar en un fichero la contraseña generada")
                    # OBTENCION DE LOS DATOS NECESARIOS PARA PODER GUARDAR LA CONTRASEÑA
                    nombre_fichero = input("¿Como se llama el fichero donde quieres guardar la contraseña? (no incluir la extension del fichero)")
                    # LLAMAMIENTO A LA FUNCION ENCARGADA DE ALMACENAR LA CONTRASEÑA
                    guardad_contraseña(nombre_fichero, contraseña)
                else:
                    print("No se ha podido realizar la operacion. Motivo: Actualmente no hay ninguna contraseña que guardar.")
            case 3:
                print("De acuerdo, vamos a recuperar la contraseña. Necesito estos datos:")
                fichero_recuperar = input("¿Como se llama el fichero en el que se encuentra la contraseña?")
                # EJECUCION DE LA FUNCION ENCARGADA DE LA RECUPERACION DE LA CONTRASEÑA
                contraseña_recuperada = recuperar_contraseña(fichero_recuperar)
                # MOSTRARLE AL USUARIO LA CONTRASEÑA RECUPERADA
                print(f"La contraseña recuperada es: {contraseña_recuperada}")
            case 4:
                print("De acuerdo, vamos a buscar la contraseña, antes necesito los siguientes datos: ")
                # OBTENCION DE LOS DATOS NECESARIOS PARA REALIZAR LA BUSQUEDA DE LA CONTRASEÑA
                contraseña_buscar = input("¿Cuál es la contraseña que quieres buscar? ")
                fichero_buscar = input("¿En que fichero tengo que buscar la contraseña? ")
                busqueda_contraseña = buscar_contraseña(contraseña_buscar, fichero_buscar)
                print(busqueda_contraseña)
            case 5:
                break
        # VOLVER A PREGUNTAR AL USUARIO QUE OPCION DEL PROGRAMA QUIERE EJECUTAR
        seleccion_usuario = int(input(
        """
        Bienvenido a tu gestor de contraseñas, que desear realizar?
        1. Generar contraseña
        2. Guardar contraseña en un fichero
        3. Recuperar contraseña de fichero
        4. Buscar contraseña en fichero
        5. Salir
        """
        ))
    
main()