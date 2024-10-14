tu_edad = int(input("¿Cuántos años tienes? "))

match tu_edad:
    case 10:
        print("Todavia eres muy pequeño.")
    case 15:
        print("Eres un adolescente.")
    case 18: 
        print("Ya eres mayor de edad.")
    # CODIGO QUE SE EJECUTARA EN CASO DE QUE EL VALOR DE TU_EDAD NO ESTE DEFINIDO EN NINGUN CASE
    case _:
        print("Tu edad no esta catalogada.")