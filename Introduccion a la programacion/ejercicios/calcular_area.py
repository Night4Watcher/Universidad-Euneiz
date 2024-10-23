import math

def calcular_perimetro_cuadrado(lado):
    formula = lado * 4
    return formula

def calcular_area_cuadrado(lado):
    formula = lado * lado
    return formula

def calcular_area_rectangulo(base, altura):
    formula = base * altura
    return formula

def calcular_perimetro_rectangulo(base, altura):
    formula = (2 * base) + (2 * altura)
    return formula

def calcular_perimetro_circulo(diametro):
    formula = diametro * math.pi
    return formula

def calcular_area_circulo(radio):
    formula = (radio * radio) * math.pi
    return formula

def main():
    match_case = 0
    seleccion_usuario=input("¿Que quieres calcular un area o un perimetro?\n"
                            "[P] --> Perimetro\n"
                            "[A] --> Area\n")
    while seleccion_usuario.upper() != "A" and seleccion_usuario.upper() != "P":
        print("Lo que has introducido no es valido, respone con una P o una A por favor")
        seleccion_usuario=input("¿Que quieres calcular un area o un perimetro?\n"
                            "[P] --> Perimetro\n"
                            "[A] --> Area\n")
    if seleccion_usuario.upper() == "P":
        seleccion_usuario = "perimetro"
        match_case = 1
    elif seleccion_usuario.upper() == "A":
        seleccion_usuario = "area"
        match_case = 2
    seleccion_figura=input(f"¿De que figura quieres calcular el {seleccion_usuario} un area o un perimetro?\n"
                            "[C] --> Circulo\n"
                            "[R] --> Cuadrado\n"
                            "[V] --> Rectangulo\n")
    while seleccion_figura.upper() != "C" and seleccion_figura.upper() != "R":
        print("Lo que has introducido no es valido, respone con una C o una R por favor")
        seleccion_figura=input(f"¿De que figura quieres calcular el {seleccion_usuario} un area o un perimetro?\n"
                            "[C] --> Circulo\n"
                            "[R] --> Cuadrado\n"
                            "[V] --> Rectangulo\n")
    match match_case:
        case 1:
            if seleccion_figura.upper() == "R":
                print("Vamos a calcular el perimetro de un cuadrado.")
                lado_cuadrado = int(input("¿cuanto mide el lado del cuadrado? "))
                print(f"El perimetro del cuadrado es: {calcular_perimetro_cuadrado(lado_cuadrado)}")
            elif seleccion_figura.upper() == "C":
                print("Vamos a calcular el perimetro de un circulo.")
                radio_circulo = int(input("¿Cuanto mide el diametro del circulo? "))
                print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio_circulo)}")
            elif seleccion_figura.upper() == "V":
                print("Vamos a calcular el perimetro de un rectangulo")
                base_rectangulo = int(input("¿Cuanto mide la base del rectangulo? "))
                altura_rectangulo = int(input("¿Cuanto mide la altura del rectangulo? "))
                print(f"El perimetro del rectangulo es: {calcular_perimetro_rectangulo(base_rectangulo, altura_rectangulo)}")
        case 2:
            if seleccion_figura.upper() == "R":
                print("Vamos a calcular el area de un cuadrado.")
                lado_cuadrado = int(input("¿cuanto mide el lado del cuadrado? "))
                print(f"El area del cuadrado es: {calcular_area_cuadrado(lado_cuadrado)}")
            elif seleccion_figura.upper() == "C":
                print("Vamos a calcular el area de un circulo.")
                radio_circulo = int(input("¿Cuanto mide el diametro del circulo? "))
                print(f"El area del circulo es: {calcular_area_circulo(radio_circulo)}")
            elif seleccion_figura.upper() == "V":
                print("Vamos a calcular el area de un rectangulo")
                base_rectangulo = int(input("¿Cuanto mide la base del rectangulo? "))
                altura_rectangulo = int(input("¿Cuanto mide la altura del rectangulo? "))
                print(f"El area del rectangulo es: {calcular_area_rectangulo(base_rectangulo, altura_rectangulo)}")
    
main()
