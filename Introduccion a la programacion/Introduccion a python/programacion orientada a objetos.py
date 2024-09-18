# OBJETO LLAMADO ANIMAL CREADO Y SUS POSIBLES CARACTERISTICAS Y "CAPACIDADES"
class Animal:
    def __init__(self, tipo_animal, nombre, raza):
        self.tipo_animal = tipo_animal
        self.nombre = nombre
        self.raza = raza
    
    def nombramiento(self):
        print(f"Mi animal es un: {self.tipo_animal}\n"
              f"Su nombre es: {self.nombre}\n"
              f"Su raza es: {self.raza}")
    
    def ruido(self):
        if self.tipo_animal == "perro":
            print(f"{self.nombre}, que es un {self.raza} ha decidido: Ladrar")
        elif self.tipo_animal == "gato":
            print(f"{self.nombre}, que es un {self.raza} ha decidido: maullar")
            
# DEFINICION DE LA CARACTERISTICA DE TIPO DE ANIMAL POR EL USUARIO EN FUNCION A LA LISTA DE ANIMALES POSIBLES
lista_animales_posibles = ["GATO", "PERRO"]
mi_animal = input("¿Qué tipo de animal tienes en casa? ")

while mi_animal.upper() not in lista_animales_posibles:
    print("Lo sentimos, este programa unicamente esta disponible para perros y gatos")
    mi_animal = input("¿Qué tiene un perro o un gato? ")

# DEFINICION DE LA CARACTERISTICA DE RAZA DEL ANIMAL EN FUNCION AL TIPO DE ANIMAL Y LA LISTA DE RAZAS DISPONIBLES POR EL USUARIO
razas_perros = ["LABRADOR", "BORDER COLLIE", "BORDERCOLLIE", "BULLDOG", "PASTOR ALEMAN", "PASTORALEMAN"]
razas_gatos = ["RAGDOLL", "GATO PERSA", "BURMÉS", "SCOTTISH FOLD"]
raza_animal = input("¿Cuál es la raza de tu animal? ")

if mi_animal.upper() == "PERRO":
    while raza_animal.upper() not in razas_perros:
        print("Lo sentimos, esa no es una raza de perros que tengamos disponibles.")
        raza_animal = input("Por favor, pruebe de nuevo: ")
elif mi_animal.upper() == "GATO":
    while raza_animal.upper() not in razas_gatos:
        print("Lo sentimos, esa no es una raza de gatos que tengamos disponible.")
        raza_animal = input("Por favor, pruebe de nuevo: ")
        
# DEFINICION DE LA CARACTERISTICA DEL NOMBRE DEL ANIMAL POR EL USUARIO
nombre_animal = input("¿Cuál es el nombre de tu animal?")

animal_terminado = Animal(mi_animal.capitalize(), nombre_animal.capitalize(), raza_animal.capitalize())

animal_terminado.nombramiento()