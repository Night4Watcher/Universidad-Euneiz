# OPERADORES LOGICOS EN PYTHON

n1 = int(input("Dame un numero: "))
n2= int(input("Dame un numero: "))

operacion = input("¿Que operacion quieres realizar? ")

# VAMOS A HACER UNA SUMA
suma = n1 + n2
while operacion.upper() != "Q":
    if operacion.upper() == "SUMA" or operacion.upper() == "SUMAR":
        suma = n1 + n2
        print(f"De acuerdo, el resultado de la suma es: {suma}")
    elif operacion.upper() == "RESTA" or operacion.upper() == "RESTAR":
        resta = n1 - n2
        print(f"De acuerdo, el resultado de la resta es: {resta}")
    elif operacion.upper() == "DIVISION":
        division = n1 / n2
        print(f"De acuerdo, el resultado de la division es: {division}")
    elif operacion.upper() == "MULTIPLICACION" or operacion.upper() == "MULTIPLICAR":
        multiplicar = n1 * n2
        print(f"De acuerdo, el resultado de la multiplicacion es: {multiplicar}")
    elif operacion.upper() == "Q":
        break
    
    operacion = input("¿Que operacion quieres realizar? ")
    if operacion.upper() != "Q":
        cambio_numeros = input("¿Quieres cambiar los numeros con los que hacer las operaciones? ")
        if cambio_numeros.upper() == "SI":
            n1 = int(input("Dame un numero: "))
            n2= int(input("Dame un numero: "))
        elif cambio_numeros.upper() == "NO":
            print("De acuerdo, utilizaremos los mismos numeros")
            input("Pulsa enter para continuar...")
    elif operacion.upper() == "Q":
        break