import random
import string

ABECEDARIO_MINUSCULA = string.ascii_lowercase
ABECEDARIO_MAYUSCULA = string.ascii_uppercase
NUMEROS = string.digits
LONGITUD_CONTRASEÑA = 12
MAYUSCULAS_CONTRASEÑA = 1
MINUSCULAS_CONTRASEÑA = 1
NUMEROS_CONTRASEÑA = 1

def comprobacion_cantidad(cantidad):
    """
    Esta funcion esta encargada de que el valor introducido por el usuario cumpla con que sea un valor
    numerico y su tipo de dato sea un entero de valor positivo.
    
    Keyword arguments:
    argument: Es el valor introducido por el usuario cuando se le pregunta cuantas contraseñas quiere crear
    Return: Devuelve el numero de la cantidad de contraseñas que se van a crear
    """
    
    cantidad = str(cantidad)
    # COMPROBACION DE QUE LA CONTRASEÑA SEA DE VALOR NUMERICO
    while cantidad.isnumeric() == False:
        print("La contraseña tiene que ser numerica, no vale que contenga texto.")
        cantidad = input("Dame un numero de contraseñas que quieras crear: ")
    # COMPROBACION DE QUE LA CONTRASEÑA SEA MAYOR DE VALOR POSITIVO
    cantidad = int(cantidad)
    while cantidad < 0:
        print("La cantidad de contraseñas no puede tener un valor negativo.")
        cantidad = int(input("Dame un numero de contraseñas que quieras crear: "))
    # DEVOLUCION DE LA CONTRASEÑA CUMPLIENDO CON LO QUE NECESITA TENER
    return cantidad

def generador_contraseña():
    """
    Esta funcion esta encargada de generar las contraseñas solicitadas por el usuario mediante unos requisitos
    minimos de longitud de caracteres y contenido de los caracteres.
    
    Keyword arguments:
    argument -- Ningun argumento
    Return: Devuelve la contraseña que cumple con los requisitos minimos
    """
    
    # VARIABLES RELACIONADAS CON EL GENERADOR DE CONTRASEÑAS
    contraseña = ""
    cant_mayusculas = 0
    cant_minusculas = 0
    cant_numeros = 0
    cant_caracteres = cant_minusculas + cant_mayusculas + cant_numeros
    # BUCLE QUE COMPRUEBA QUE LA CONTRASEÑA QUE SE VAYA A DEVOLVER CUMPLA CON UNAS CARACTERISTICAS
    while cant_caracteres < LONGITUD_CONTRASEÑA or cant_numeros < NUMEROS_CONTRASEÑA or cant_mayusculas < MAYUSCULAS_CONTRASEÑA:
        # RESETEO DE LAS VARIABLES PARA QUE NO SE ACUMULEN LOS DISTINTOS INTENTOS ALMACENADOS
        cant_mayusculas = 0
        cant_minusculas = 0
        cant_numeros = 0
        # CREACION DEL CARACTER A AÑADIR DE MANERA ALEATORIA
        char_create = random.randint(0, 2)
        # CREACION DEL CARACTER EN MINUSCULA
        if char_create == 0:
            min_create = random.choice(ABECEDARIO_MINUSCULA)
            contraseña = contraseña + min_create
        # CREACION DEL CARACTER EN MAYUSCULA
        elif char_create == 1:
            mayus_create = random.choice(ABECEDARIO_MAYUSCULA)
            contraseña = contraseña + mayus_create
        # CREACION DEL CARACTER NUMERICO
        elif char_create == 2:
            num_create = random.choice(NUMEROS)
            contraseña = contraseña + num_create
        for character in contraseña:
            if character.isdigit():
                cant_numeros += 1
            elif character in ABECEDARIO_MAYUSCULA:
                cant_mayusculas += 1
            elif character in ABECEDARIO_MINUSCULA:
                cant_minusculas += 1
        cant_caracteres = cant_minusculas + cant_mayusculas + cant_numeros
    # DEVOLVER LA CONTRASEÑA QUE CUMPLE CON LOS REQUISITOS SOLICITADOS
    return contraseña

def main():
    cantidad_contraseñas = 0
    contraseñas = []
    # BIENVENIDA DEL USUARIO AL PROGRAMA
    print("Bienvenido a tu generador de contraseñas personal.")
    input("Pulsa enter para continuar...")
    # PREGUNTAR AL USUARIO CUANTAS CONTRASEÑAS QUIERE CREAR
    cantidad_contraseñas = input("¿Cuantas contraseñas quieres que te genere el programa? ")
    # EJECUTAMOS LA FUNCION PARA COMPROBAR QUE EL DATO INTRODUCIDO POR EL USUARIO CUMPLE CON LO NECESARIO
    cantidad_contraseñas = comprobacion_cantidad(cantidad_contraseñas)
    # BUCLE DEL PROGAMA HASTA CREAR TODAS LAS CONTRASEÑAS QUE QUIERE EL USUARIO
    while cantidad_contraseñas > 0:
        contraseñas.append(generador_contraseña())
        cantidad_contraseñas -= 1
    print(f"Las contraseñas generadas han sido: {contraseñas}")
    

main()