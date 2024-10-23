def numero_minimo(lista):
    numero_mas_pequeño = lista[0]
    for numero in lista:
        if numero_mas_pequeño > numero:
            numero_mas_pequeño = numero
    return numero_mas_pequeño

def numero_maximo(lista):
    numero_mas_grande = lista[0]
    for numero in lista:
        if numero_mas_grande < numero:
            numero_mas_grande = numero
    return numero_mas_grande

def suma_todos(lista):
    suma_total = 0
    for numero in lista:
        suma_total = suma_total + numero
    return suma_total

def multiplicacion_todos(lista):
    multiplicacion_total = 1
    for numero in lista:
        multiplicacion_total = multiplicacion_total * numero
    return multiplicacion_total

def main():
    lista_numeros = []
    input_usuario = int(input("¿Cuantos numeros quieres introducir?"))
    while input_usuario > 0:
        numero = int(input("Dame un numero: "))
        lista_numeros.append(numero)
        input_usuario -= 1
    print(f"1. El numero mas pequeño de la lista es: {numero_minimo(lista_numeros)}")
    print(f"2. El numero mas grande es: {numero_maximo(lista_numeros)}")
    print(f"3. La suma de todos los numero es: {suma_todos(lista_numeros)}")
    print(f"La multiplicacion de todos los numeros es: {multiplicacion_todos(lista_numeros)}")

main()
