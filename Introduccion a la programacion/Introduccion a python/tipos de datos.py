# PRUEBAS CON LOS TIPOS DE DATOS

x = int(input("Dame un numero: "))
y = input("Dame una palabra o una frase: ")

print(type(y))

if type(x) == int:
    print("La variable X es un entero")
else:
    print("No se que tipo de variable es X")

if type(y) == str:
    print("La variable y es una string")
else:
    print("No se que tipo de variable es X")    
