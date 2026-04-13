from array_propio import *
from linkedlist import *

class cancion:
    def __init__(self, nombre_cancion):
        self.nombre_cancion = nombre_cancion
        self.siguiente_cancion = None

    def __repr__(self):
        return self.nombre_cancion