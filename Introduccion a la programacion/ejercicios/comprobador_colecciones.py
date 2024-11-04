coleccion = [1, 4, 5, 9]

def comprobador(coleccion, valor):
    return valor in coleccion

def main():
    valor_comprobar = int(input("Dame un valor para comprobarlo en la coleccion: "))
    print(comprobador(coleccion, valor_comprobar))

main()