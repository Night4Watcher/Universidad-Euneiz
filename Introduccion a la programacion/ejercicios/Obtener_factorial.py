def factorial(numero):
    numero = numero + 1
    resultado = 1
    for n in range(numero):
        if n != 0:
            resultado = resultado * n
    return resultado

def main():
    numero = int(input("Dame un numero del que hacer el numero factorial: "))
    while numero <= 0:
        print("El numero no puede ser negativo")
        numero = int(input("Dame un numero del que hacer el numero factorial: "))
    print(f"El factorial de {numero} es {factorial(numero)}")

main()