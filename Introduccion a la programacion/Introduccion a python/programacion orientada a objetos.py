class Animal:
    def __init__(self, tipo_animal, nombre, raza):
        self.tipo_animal = tipo_animal
        self.nombre = nombre
        self.raza = raza
    
    def ruido(self):
        if self.tipo_animal == "perro":
            print(f"{self.nombre}, que es un {self.raza} ha decidido: Ladrar")
        elif self.tipo_animal == "gato":
            print(f"{self.nombre}, que es un {self.raza} ha decidido: maullar")
            
lista_animales_posibles = ["GATO, PERRO"]
mi_animal = input("¿Qué tipo de animal tienes en casa? ")

while mi_animal.upper() not in lista_animales_posibles:
    print("Lo sentimos, este programa unicamente esta disponible para perros y gatos")
    mi_animal = input("¿Qué tiene un perro o un gato?")
    
