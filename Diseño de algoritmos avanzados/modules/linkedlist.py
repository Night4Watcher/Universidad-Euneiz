from nodo import cancion

class playlist:
    def __init__(self, canciones=None):
        self.head = canciones
        if canciones == None:
            self.longitud = 0
        else:
            self.longitud = 1

    def Insertar_cancion(self, cancion_nueva, posicion):
        # Levantar error en caso de que la posicion este fuera del indice
        if posicion < 1 or posicion > self.longitud:
            raise IndexError(f"La posicion {posicion} esta fuera del rango de la lista. Rango: 1 {self.longitud + 1}")
        # Creamos el objeto posicion que vamos a añadir a la LinkedList
        cancion_para_añadir = cancion(cancion_nueva)

        if posicion == 1:
            cancion_para_añadir.siguiente_cancion = self.head
            self.head = cancion_para_añadir
        else:
            elemento_actual = self.head
            i=1
            # Bucle para llegar a la posicion donde se quiere añadir la nueva cancion
            while i < posicion - 1:
                elemento_actual = elemento_actual.siguiente_cancion
                i += 1
            # Insertamos la cancion en la posicion
            cancion_para_añadir.siguiente_cancion = elemento_actual
            elemento_actual.siguiente_cancion = cancion_para_añadir
        self.longitud += 1

    def __repr__(self):
        pass