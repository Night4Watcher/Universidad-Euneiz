# OPERADORES LOGICOS EN PYTHON

n1 = int(input("Dame un numero: "))
n2= int(input("Dame un numero: "))

operacion = input("¿Que operacion quieres realizar? ")

# SELECCION DE LA OPERACION QUE QUEREMOS REALIZAR
suma = n1 + n2
while operacion.upper() != "Q":
    # REALIZAR UNA SUMA
    if operacion.upper() == "SUMA" or operacion.upper() == "SUMAR":
        suma = n1 + n2
        print(f"De acuerdo, el resultado de la suma es: {suma}")
    # REALIZAR UNA RESTA
    elif operacion.upper() == "RESTA" or operacion.upper() == "RESTAR":
        resta = n1 - n2
        print(f"De acuerdo, el resultado de la resta es: {resta}")
    # REALIZAR UNA DIVISION
    elif operacion.upper() == "DIVISION":
        division = n1 / n2
        print(f"De acuerdo, el resultado de la division es: {division}")
    # REALIZAR UNA MULTIPLICACION
    elif operacion.upper() == "MULTIPLICACION" or operacion.upper() == "MULTIPLICAR":
        multiplicar = n1 * n2
        print(f"De acuerdo, el resultado de la multiplicacion es: {multiplicar}")
    # REALIZAR UN MODULO
    elif operacion.upper() == "MODULO":
        modulo = n1 % n2
        print(f"De acuerdo, el resultado del modulo es: {modulo}")
    # NO REALIZAR NADA Y SALIR DEL PROGRAMA
    elif operacion.upper() == "Q":
        break
    
    # COMPROBAR SI SE QUIERE REALIZAR ALGUNA OPERACION MAS
    operacion = input("¿Que operacion quieres realizar? ")
    if operacion.upper() != "Q":
        # COMPROBAR SI SE QUIEREN CAMBIAR LOS NUMEROS CON LOS QUE REALIZAR LAS OPERACIONES
        cambio_numeros = input("¿Quieres cambiar los numeros con los que hacer las operaciones? ")
        if cambio_numeros.upper() == "SI":
            n1 = int(input("Dame un numero: "))
            n2= int(input("Dame un numero: "))
        elif cambio_numeros.upper() == "NO":
            print("De acuerdo, utilizaremos los mismos numeros")
            input("Pulsa enter para continuar...")
    elif operacion.upper() == "Q":
        break