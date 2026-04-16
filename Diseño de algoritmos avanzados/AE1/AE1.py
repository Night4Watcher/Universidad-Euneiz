import time
import csv
from pathlib import Path
import matplotlib.pyplot as plt


# ============================================================
# 1. EXCEPCIONES
# ============================================================
class ListaVaciaError(Exception):
    pass


class PosicionInvalidaError(Exception):
    pass


# ============================================================
# 2. TDA LISTA CON ARRAYS
# Restricción: no usar append(), insert(), pop(), remove(), extend()
# ============================================================
class ListaArray:
    def __init__(self):
        self.Crear()

    def Crear(self):
        self._datos = []
        self._n = 0

    def Longitud(self):
        return self._n

    def EsVacia(self):
        return self._n == 0

    def Insertar(self, e, p):
        if p < 0 or p > self._n:
            raise PosicionInvalidaError("Posición inválida.")

        nuevo = [None] * (self._n + 1)

        i = 0
        while i < p:
            nuevo[i] = self._datos[i]
            i += 1

        nuevo[p] = e

        while i < self._n:
            nuevo[i + 1] = self._datos[i]
            i += 1

        self._datos = nuevo
        self._n += 1

    def Eliminar(self, p):
        if self.EsVacia():
            raise ListaVaciaError("La lista está vacía.")
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")

        eliminado = self._datos[p]
        nuevo = [None] * (self._n - 1)

        i = 0
        while i < p:
            nuevo[i] = self._datos[i]
            i += 1

        while i < self._n - 1:
            nuevo[i] = self._datos[i + 1]
            i += 1

        self._datos = nuevo
        self._n -= 1
        return eliminado

    def Buscar(self, e):
        i = 0
        while i < self._n:
            if self._datos[i] == e:
                return i
            i += 1
        return -1

    def Obtener(self, p):
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")
        return self._datos[p]

    def Actualizar(self, p, e):
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")
        self._datos[p] = e

    def __str__(self):
        texto = "["
        i = 0
        while i < self._n:
            texto += str(self._datos[i])
            if i < self._n - 1:
                texto += ", "
            i += 1
        texto += "]"
        return texto


# ============================================================
# 3. TDA LISTA CON LISTA ENLAZADA
# ============================================================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.Crear()

    def Crear(self):
        self._cabeza = None
        self._n = 0

    def Longitud(self):
        return self._n

    def EsVacia(self):
        return self._n == 0

    def Insertar(self, e, p):
        if p < 0 or p > self._n:
            raise PosicionInvalidaError("Posición inválida.")

        nuevo = Nodo(e)

        if p == 0:
            nuevo.sig = self._cabeza
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            i = 0
            while i < p - 1:
                actual = actual.sig
                i += 1
            nuevo.sig = actual.sig
            actual.sig = nuevo

        self._n += 1

    def Eliminar(self, p):
        if self.EsVacia():
            raise ListaVaciaError("La lista está vacía.")
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")

        if p == 0:
            eliminado = self._cabeza.dato
            self._cabeza = self._cabeza.sig
        else:
            actual = self._cabeza
            i = 0
            while i < p - 1:
                actual = actual.sig
                i += 1
            eliminado = actual.sig.dato
            actual.sig = actual.sig.sig

        self._n -= 1
        return eliminado

    def Buscar(self, e):
        actual = self._cabeza
        i = 0
        while actual is not None:
            if actual.dato == e:
                return i
            actual = actual.sig
            i += 1
        return -1

    def Obtener(self, p):
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")

        actual = self._cabeza
        i = 0
        while i < p:
            actual = actual.sig
            i += 1
        return actual.dato

    def Actualizar(self, p, e):
        if p < 0 or p >= self._n:
            raise PosicionInvalidaError("Posición inválida.")

        actual = self._cabeza
        i = 0
        while i < p:
            actual = actual.sig
            i += 1
        actual.dato = e

    def __str__(self):
        texto = "["
        actual = self._cabeza
        while actual is not None:
            texto += str(actual.dato)
            if actual.sig is not None:
                texto += ", "
            actual = actual.sig
        texto += "]"
        return texto


# ============================================================
# 4. MODELOS DEL DOMINIO
# ============================================================
class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion})"

    def __eq__(self, other):
        return (
            isinstance(other, Cancion)
            and self.titulo.lower() == other.titulo.lower()
            and self.artista.lower() == other.artista.lower()
            and self.duracion == other.duracion
        )


class Playlist:
    def __init__(self, nombre, tipo_lista):
        self.nombre = nombre
        self._tipo_lista = tipo_lista
        self._canciones = tipo_lista()

    def agregar_cancion(self, cancion):
        self._canciones.Insertar(cancion, self._canciones.Longitud())

    def insertar_cancion(self, cancion, posicion):
        self._canciones.Insertar(cancion, posicion)

    def eliminar_cancion(self, posicion):
        return self._canciones.Eliminar(posicion)

    def obtener_cancion(self, posicion):
        return self._canciones.Obtener(posicion)

    def actualizar_cancion(self, posicion, nueva_cancion):
        self._canciones.Actualizar(posicion, nueva_cancion)

    def longitud(self):
        return self._canciones.Longitud()

    def esta_vacia(self):
        return self._canciones.EsVacia()

    def buscar_por_titulo(self, titulo):
        i = 0
        while i < self._canciones.Longitud():
            cancion = self._canciones.Obtener(i)
            if cancion.titulo.lower() == titulo.lower():
                return i, cancion
            i += 1
        return -1, None

    def mover_cancion(self, origen, destino):
        if origen < 0 or origen >= self._canciones.Longitud():
            raise PosicionInvalidaError("Posición de origen inválida.")
        if destino < 0 or destino > self._canciones.Longitud():
            raise PosicionInvalidaError("Posición de destino inválida.")

        cancion = self._canciones.Eliminar(origen)

        if destino > self._canciones.Longitud():
            destino = self._canciones.Longitud()

        self._canciones.Insertar(cancion, destino)

    def mostrar(self):
        if self._canciones.EsVacia():
            print("La playlist está vacía.")
            return

        i = 0
        while i < self._canciones.Longitud():
            print(f"{i}. {self._canciones.Obtener(i)}")
            i += 1


# ============================================================
# 5. SERVICIO DE GESTIÓN
# ============================================================
class GestorPlaylists:
    def __init__(self, tipo_lista):
        self._tipo_lista = tipo_lista
        self._playlists = tipo_lista()

    def crear_playlist(self, nombre):
        playlist = Playlist(nombre, self._tipo_lista)
        self._playlists.Insertar(playlist, self._playlists.Longitud())

    def agregar_playlist_existente(self, playlist):
        self._playlists.Insertar(playlist, self._playlists.Longitud())

    def listar_playlists(self):
        if self._playlists.EsVacia():
            print("No hay playlists creadas.")
            return

        i = 0
        while i < self._playlists.Longitud():
            playlist = self._playlists.Obtener(i)
            print(f"{i}. {playlist.nombre} ({playlist.longitud()} canciones)")
            i += 1

    def obtener_playlist(self, posicion):
        return self._playlists.Obtener(posicion)

    def eliminar_playlist(self, posicion):
        return self._playlists.Eliminar(posicion)

    def buscar_playlist_por_nombre(self, nombre):
        i = 0
        while i < self._playlists.Longitud():
            playlist = self._playlists.Obtener(i)
            if playlist.nombre.lower() == nombre.lower():
                return i, playlist
            i += 1
        return -1, None

    def total_playlists(self):
        return self._playlists.Longitud()

    def cargar_demos(self):
        demos = construir_playlists_demo(self._tipo_lista)
        i = 0
        while i < len(demos):
            self.agregar_playlist_existente(demos[i])
            i += 1


# ============================================================
# 6. DATOS DEMO
# ============================================================
def construir_playlists_demo(tipo_lista):
    playlist1 = Playlist("Rock clásico", tipo_lista)
    playlist1.agregar_cancion(Cancion("Bohemian Rhapsody", "Queen", "05:55"))
    playlist1.agregar_cancion(Cancion("Hotel California", "Eagles", "06:30"))
    playlist1.agregar_cancion(Cancion("Smoke on the Water", "Deep Purple", "05:40"))

    playlist2 = Playlist("Pop actual", tipo_lista)
    playlist2.agregar_cancion(Cancion("Blinding Lights", "The Weeknd", "03:20"))
    playlist2.agregar_cancion(Cancion("Levitating", "Dua Lipa", "03:23"))
    playlist2.agregar_cancion(Cancion("As It Was", "Harry Styles", "02:47"))

    playlist3 = Playlist("Estudio / Concentración", tipo_lista)
    playlist3.agregar_cancion(Cancion("Experience", "Ludovico Einaudi", "05:15"))
    playlist3.agregar_cancion(Cancion("Nuvole Bianche", "Ludovico Einaudi", "05:57"))
    playlist3.agregar_cancion(Cancion("Comptine d'un autre été", "Yann Tiersen", "02:21"))

    return [playlist1, playlist2, playlist3]


# ============================================================
# 7. UTILIDADES
# ============================================================
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debes introducir un número entero.")


def pausar():
    input("\nPulsa ENTER para continuar...")


def leer_cancion_desde_teclado():
    titulo = input("Título: ")
    artista = input("Artista: ")
    duracion = input("Duración (mm:ss): ")
    return Cancion(titulo, artista, duracion)


def generar_cancion_demo(i):
    return Cancion(f"Cancion_{i}", f"Artista_{i}", f"03:{i % 60:02d}")


# ============================================================
# 8. BENCHMARK
# ============================================================
def medir_operacion(funcion, repeticiones=3):
    total = 0.0
    i = 0
    while i < repeticiones:
        inicio = time.perf_counter()
        funcion()
        fin = time.perf_counter()
        total += (fin - inicio)
        i += 1
    return total / repeticiones


def benchmark_insertar_final(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            playlist.agregar_cancion(generar_cancion_demo(i))
            i += 1
    return medir_operacion(prueba)


def benchmark_insertar_medio(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            pos = playlist.longitud() // 2
            playlist.insertar_cancion(generar_cancion_demo(i), pos)
            i += 1
    return medir_operacion(prueba)


def benchmark_busqueda(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            playlist.agregar_cancion(generar_cancion_demo(i))
            i += 1
        if n > 0:
            playlist.buscar_por_titulo(f"Cancion_{n - 1}")
    return medir_operacion(prueba)


def benchmark_obtener(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            playlist.agregar_cancion(generar_cancion_demo(i))
            i += 1
        if n > 0:
            playlist.obtener_cancion(n // 2)
    return medir_operacion(prueba)


def benchmark_actualizar(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            playlist.agregar_cancion(generar_cancion_demo(i))
            i += 1
        if n > 0:
            playlist.actualizar_cancion(n // 2, Cancion("Nueva", "Actualizada", "04:00"))
    return medir_operacion(prueba)


def benchmark_eliminar_medio(tipo_lista, n):
    def prueba():
        playlist = Playlist("Benchmark", tipo_lista)
        i = 0
        while i < n:
            playlist.agregar_cancion(generar_cancion_demo(i))
            i += 1
        if n > 0:
            playlist.eliminar_cancion(n // 2)
    return medir_operacion(prueba)


def guardar_csv_dicts(nombre_archivo, filas):
    if not filas:
        return

    with open(nombre_archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        writer.writeheader()

        i = 0
        while i < len(filas):
            writer.writerow(filas[i])
            i += 1


def generar_grafica(nombre_operacion, xs, ys_array, ys_enlazada, ruta_salida):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, ys_array, marker="o", label="Array")
    plt.plot(xs, ys_enlazada, marker="s", label="Lista enlazada")
    plt.title(f"{nombre_operacion} vs tamaño")
    plt.xlabel("Tamaño n")
    plt.ylabel("Tiempo (s)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()


def ejecutar_benchmark_completo():
    salida = Path("output")
    salida.mkdir(exist_ok=True)

    tamanos = [1, 10, 100, 1000, 5000]
    pruebas = [
        ("insertar_final", benchmark_insertar_final),
        ("insertar_medio", benchmark_insertar_medio),
        ("buscar", benchmark_busqueda),
        ("obtener", benchmark_obtener),
        ("actualizar", benchmark_actualizar),
        ("eliminar_medio", benchmark_eliminar_medio),
    ]

    resultados_ancho = []
    resultados_largo = []

    print("\n=== BENCHMARK COMPLETO ===")
    print("Se generarán CSV y gráficas PNG en la carpeta output.\n")

    j = 0
    while j < len(tamanos):
        n = tamanos[j]
        fila = {"n": n}
        print(f"Tamaño n = {n}")

        k = 0
        while k < len(pruebas):
            nombre, funcion = pruebas[k]

            tiempo_array = funcion(ListaArray, n)
            tiempo_enlazada = funcion(ListaEnlazada, n)

            fila[f"{nombre}_array"] = tiempo_array
            fila[f"{nombre}_enlazada"] = tiempo_enlazada

            resultados_largo.append({
                "n": n,
                "operacion": nombre,
                "implementacion": "array",
                "tiempo_segundos": tiempo_array
            })

            resultados_largo.append({
                "n": n,
                "operacion": nombre,
                "implementacion": "lista_enlazada",
                "tiempo_segundos": tiempo_enlazada
            })

            print(f"- {nombre}: array={tiempo_array:.8f}s | enlazada={tiempo_enlazada:.8f}s")
            k += 1

        resultados_ancho.append(fila)
        print()
        j += 1

    guardar_csv_dicts(salida / "benchmark_resultados_ancho.csv", resultados_ancho)
    guardar_csv_dicts(salida / "benchmark_resultados_largo.csv", resultados_largo)

    resumen = []
    i = 0
    while i < len(pruebas):
        nombre, _ = pruebas[i]

        xs = []
        ys_array = []
        ys_enlazada = []

        t = 0
        while t < len(resultados_ancho):
            fila = resultados_ancho[t]
            xs.append(fila["n"])
            ys_array.append(fila[f"{nombre}_array"])
            ys_enlazada.append(fila[f"{nombre}_enlazada"])

            resumen.append({
                "n": fila["n"],
                "operacion": nombre,
                "array": fila[f"{nombre}_array"],
                "lista_enlazada": fila[f"{nombre}_enlazada"]
            })
            t += 1

        generar_grafica(
            nombre,
            xs,
            ys_array,
            ys_enlazada,
            salida / f"benchmark_{nombre}.png"
        )
        i += 1

    guardar_csv_dicts(salida / "benchmark_resumen.csv", resumen)

    print("Archivos generados correctamente:")
    print("- output/benchmark_resultados_ancho.csv")
    print("- output/benchmark_resultados_largo.csv")
    print("- output/benchmark_resumen.csv")
    print("- output/benchmark_insertar_final.png")
    print("- output/benchmark_insertar_medio.png")
    print("- output/benchmark_buscar.png")
    print("- output/benchmark_obtener.png")
    print("- output/benchmark_actualizar.png")
    print("- output/benchmark_eliminar_medio.png")


# ============================================================
# 9. MENÚ PLAYLIST
# ============================================================
def menu_playlist(playlist):
    while True:
        print(f"\n=== PLAYLIST: {playlist.nombre} ===")
        print("1. Ver canciones")
        print("2. Agregar canción al final")
        print("3. Insertar canción en posición")
        print("4. Eliminar canción")
        print("5. Buscar canción por título")
        print("6. Actualizar canción")
        print("7. Mover canción")
        print("8. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                playlist.mostrar()
                pausar()

            elif opcion == "2":
                cancion = leer_cancion_desde_teclado()
                playlist.agregar_cancion(cancion)
                print("Canción agregada correctamente.")
                pausar()

            elif opcion == "3":
                cancion = leer_cancion_desde_teclado()
                pos = pedir_entero("Posición donde insertar: ")
                playlist.insertar_cancion(cancion, pos)
                print("Canción insertada correctamente.")
                pausar()

            elif opcion == "4":
                pos = pedir_entero("Posición de la canción a eliminar: ")
                eliminada = playlist.eliminar_cancion(pos)
                print(f"Se eliminó: {eliminada}")
                pausar()

            elif opcion == "5":
                titulo = input("Título de la canción a buscar: ")
                pos, cancion = playlist.buscar_por_titulo(titulo)
                if pos != -1:
                    print(f"Canción encontrada en la posición {pos}: {cancion}")
                else:
                    print("No se encontró la canción.")
                pausar()

            elif opcion == "6":
                pos = pedir_entero("Posición de la canción a actualizar: ")
                nueva = leer_cancion_desde_teclado()
                playlist.actualizar_cancion(pos, nueva)
                print("Canción actualizada correctamente.")
                pausar()

            elif opcion == "7":
                origen = pedir_entero("Posición de origen: ")
                destino = pedir_entero("Posición de destino: ")
                playlist.mover_cancion(origen, destino)
                print("Canción movida correctamente.")
                pausar()

            elif opcion == "8":
                break

            else:
                print("Opción no válida.")
                pausar()

        except (ListaVaciaError, PosicionInvalidaError) as e:
            print(f"Error: {e}")
            pausar()


# ============================================================
# 10. MENÚ PRINCIPAL
# ============================================================
def menu_principal(gestor):
    while True:
        print("\n=== GESTOR DE PLAYLISTS ===")
        print("1. Crear playlist vacía")
        print("2. Cargar playlists de demostración")
        print("3. Listar playlists")
        print("4. Abrir playlist")
        print("5. Eliminar playlist")
        print("6. Buscar playlist por nombre")
        print("7. Ver total de playlists")
        print("8. Ejecutar benchmark empírico")
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                nombre = input("Nombre de la nueva playlist: ")
                gestor.crear_playlist(nombre)
                print("Playlist creada correctamente.")
                pausar()

            elif opcion == "2":
                gestor.cargar_demos()
                print("Se cargaron playlists de demostración.")
                pausar()

            elif opcion == "3":
                gestor.listar_playlists()
                pausar()

            elif opcion == "4":
                if gestor.total_playlists() == 0:
                    print("No hay playlists para abrir.")
                    pausar()
                else:
                    gestor.listar_playlists()
                    pos = pedir_entero("Selecciona la posición de la playlist: ")
                    playlist = gestor.obtener_playlist(pos)
                    menu_playlist(playlist)

            elif opcion == "5":
                if gestor.total_playlists() == 0:
                    print("No hay playlists para eliminar.")
                else:
                    gestor.listar_playlists()
                    pos = pedir_entero("Selecciona la posición a eliminar: ")
                    eliminada = gestor.eliminar_playlist(pos)
                    print(f"Se eliminó la playlist: {eliminada.nombre}")
                pausar()

            elif opcion == "6":
                nombre = input("Nombre de la playlist a buscar: ")
                pos, playlist = gestor.buscar_playlist_por_nombre(nombre)
                if pos != -1:
                    print(f"Playlist encontrada en posición {pos}: {playlist.nombre}")
                else:
                    print("No se encontró la playlist.")
                pausar()

            elif opcion == "7":
                print(f"Total de playlists: {gestor.total_playlists()}")
                pausar()

            elif opcion == "8":
                ejecutar_benchmark_completo()
                pausar()

            elif opcion == "9":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida.")
                pausar()

        except (ListaVaciaError, PosicionInvalidaError) as e:
            print(f"Error: {e}")
            pausar()


# ============================================================
# 11. SELECCIÓN DE IMPLEMENTACIÓN
# ============================================================
def seleccionar_implementacion():
    while True:
        print("=== SELECCIÓN DE IMPLEMENTACIÓN DEL TDA LISTA ===")
        print("1. Implementación con arrays")
        print("2. Implementación con lista enlazada")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            return ListaArray
        elif opcion == "2":
            return ListaEnlazada
        else:
            print("Opción no válida.\n")


# ============================================================
# 12. MAIN
# ============================================================
def main():
    print("Bienvenido al gestor de playlists.")
    tipo_lista = seleccionar_implementacion()
    gestor = GestorPlaylists(tipo_lista)
    menu_principal(gestor)


if __name__ == "__main__":
    main()