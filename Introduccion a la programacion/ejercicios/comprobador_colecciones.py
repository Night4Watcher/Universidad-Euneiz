coleccion = [1, 4, 5, 9]

def comprobador(coleccion, valor):
    if valor in coleccion:
        return True
    else:
        return False

def main():
    valor_comprobar = int(input("Dame un valor para comprobarlo en la coleccion: "))
    print(comprobador(coleccion, valor_comprobar))

main()