from complubot.libreria_dodo import dodo
from machine import Pin
import time
# VARIABLE DE LA PANTALLA
mi_robot = dodo()
# VARIABLES DE LA PLACA DODOBOARD
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)

# FUNCION ENCARGADA DE MOSTRAR EL MENU INICIAL AL USUARIO Y QUE PUEDA INTERACTUAR CON EL
def mostrar_menu_inicial():
    mi_robot.borra_pantalla()
    indice_estado = 0
    posicion_x = [8, 76]
    posicion_y = [50, 50]
    estado_opciones = ['> Jugar', 'Salir', 'Jugar', '> Salir']
    # MOSTRAMOS AL USUARIO EL MENSAJE DE BIENVENIDA
    mi_robot.escribe_pantalla('Bienvenido al', 16, 0)
    mi_robot.escribe_pantalla('quiz!', 48, 14)
    mi_robot.escribe_pantalla(str(estado_opciones[indice_estado]), posicion_x[0], posicion_y[0])
    mi_robot.escribe_pantalla(str(estado_opciones[indice_estado + 1]), posicion_x[1], posicion_y[1])
    while boton_izquierda.value() != 1:
        # ALTERAR LO QUE MUESTRA LA PANTALLA SI EL USUARIO INTERACTUA
        if boton_derecha.value() == 1 and indice_estado == 0:
            indice_estado += 2
            posicion_x = [8, 68]
            mi_robot.escribe_pantalla(str(estado_opciones[indice_estado]), posicion_x[0], posicion_y[0])
            mi_robot.escribe_pantalla(str(estado_opciones[indice_estado + 1]), posicion_x[1], posicion_y[1])
        elif boton_derecha.value() == 1 and indice_estado == 2:
            indice_estado -= 2
            posicion_x = [8, 76]
            mi_robot.escribe_pantalla(str(estado_opciones[indice_estado]), posicion_x[0], posicion_y[0])
            mi_robot.escribe_pantalla(str(estado_opciones[indice_estado + 1]), posicion_x[1], posicion_y[1])
        time.sleep(0.2)
    if indice_estado == 0:
        print('Se ha seleccionado la opcion de juego')
        return 'jugar'
    elif indice_estado == 2:
        print('Se ha seleccionado la opcion de salir')
        return 'salir'
    else:
        print('Hubo un error, reiniciar')
        return 'error'

def mostrar_menu_salida():
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('Gracias por', 20, 24)
    mi_robot.escribe_pantalla('jugar!', 40, 34)
    time.sleep(5)
    
def mostrar_menu_aviso_estructura():
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('A continuacion', 10, 4)
    mi_robot.escribe_pantalla('se le mostrara', 10, 14)
    mi_robot.escribe_pantalla('la  estructura', 10, 24)
    mi_robot.escribe_pantalla('del   programa', 10, 34)
    mi_robot.escribe_pantalla('Espere........', 10, 44)
    time.sleep(5)
    
def mostrar_menu_estructura():
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('1. Pregunta a', 0, 0)
    mi_robot.escribe_pantalla('   responder:', 0, 10)
    mi_robot.escribe_pantalla('> a.Respuesta', 0, 20)
    mi_robot.escribe_pantalla('  b.Respuesta', 0, 30)
    mi_robot.escribe_pantalla('  c.Respuesta', 0, 40)
    mi_robot.escribe_pantalla('Pulsa boton sig.', 0, 50)
    while boton_derecha.value() != 1 and boton_izquierda.value() != 1:
        time.sleep(0.1)

def mostrar_menu_jugar():
    puntuacion_jugador = 0
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('Empieza    el', 0, 20)
    mi_robot.escribe_pantalla('    juego    ', 0, 30)
    time.sleep(2)
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('1.¿Cuanto es ', 0, 0)
    mi_robot.escribe_pantalla('   2 + 2?    ', 0, 10)
    mi_robot.escribe_pantalla('> a. 6       ', 0, 20)
    mi_robot.escribe_pantalla('  b. 4       ', 0, 30)
    mi_robot.escribe_pantalla('  c. 0       ', 0, 40)
    indice_seleccion = 0
    texto = [
        [
            '> a. 6       ',
            '  b. 4       ',
            '  c. 0       '],
        [
            '  a. 6       ',
            '> b. 4       ',
            '  c. 0       '],
        [
            '  a. 6       ',
            '  b. 4       ',
            '> c. 0       ']
    ]
    while boton_izquierda.value() != 1:
        coordenada = 20
        if boton_derecha.value() == 1 and indice_seleccion == 0:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 1:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 2:
            indice_seleccion = 0
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        time.sleep(0.2)
    if indice_seleccion == 0:
        respuesta = 6
    elif indice_seleccion == 1:
        respuesta = 4
    elif indice_seleccion == 2:
        respuesta = 0
    if respuesta == 4:
        puntuacion_jugador += 1
        mostrar_menu_correcta()
    else:
        mostrar_menu_incorrecto()
    
    mi_robot.escribe_pantalla('2.¿Cuanto es ', 0, 0)
    mi_robot.escribe_pantalla('   3 * 8?    ', 0, 10)
    mi_robot.escribe_pantalla('> a. 24      ', 0, 20)
    mi_robot.escribe_pantalla('  b. 54      ', 0, 30)
    mi_robot.escribe_pantalla('  c. 1       ', 0, 40)
    indice_seleccion = 0
    texto = [
        [
            '> a. 24      ',
            '  b. 54      ',
            '  c. 1       '],
        [
            '  a. 24      ',
            '> b. 54      ',
            '  c. 1       '],
        [
            '  a. 24      ',
            '  b. 54      ',
            '> c. 1       ']
    ]
    while boton_izquierda.value() != 1:
        coordenada = 20
        if boton_derecha.value() == 1 and indice_seleccion == 0:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 1:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 2:
            indice_seleccion = 0
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        time.sleep(0.2)
    if indice_seleccion == 0:
        respuesta = 24
    elif indice_seleccion == 1:
        respuesta = 54
    elif indice_seleccion == 2:
        respuesta = 1
    if respuesta == 24:
        puntuacion_jugador += 1
        mostrar_menu_correcta()
    else:
        mostrar_menu_incorrecto()
    
    mi_robot.escribe_pantalla('3.¿Cuanto es ', 0, 0)
    mi_robot.escribe_pantalla('   Log(2)?   ', 0, 10)
    mi_robot.escribe_pantalla('> a. 0,3010  ', 0, 20)
    mi_robot.escribe_pantalla('  b. 625     ', 0, 30)
    mi_robot.escribe_pantalla('  c. 442     ', 0, 40)
    indice_seleccion = 0
    texto = [
        [
            '> a. 0,3010  ',
            '  b. 625     ',
            '  c. 442     '],
        [
            '  a. 0,3010  ',
            '> b. 625     ',
            '  c. 442     '],
        [
            '  a. 0,3010  ',
            '  b. 625     ',
            '> c. 442     ']
    ]
    while boton_izquierda.value() != 1:
        coordenada = 20
        if boton_derecha.value() == 1 and indice_seleccion == 0:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 1:
            indice_seleccion += 1
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        elif boton_derecha.value() == 1 and indice_seleccion == 2:
            indice_seleccion = 0
            for opcion in texto[indice_seleccion]:
                mi_robot.escribe_pantalla(opcion, 0, coordenada)
                coordenada += 10
        time.sleep(0.2)
    if indice_seleccion == 0:
        respuesta = 0.3010
    elif indice_seleccion == 1:
        respuesta = 625
    elif indice_seleccion == 2:
        respuesta = 442
    if respuesta == 0.3010:
        puntuacion_jugador += 1
        mostrar_menu_correcta()
    else:
        mostrar_menu_incorrecto()
    return puntuacion_jugador
    
def mostrar_menu_correcta():
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('*************', 0, 0)
    mi_robot.escribe_pantalla('*           *', 0, 10)
    mi_robot.escribe_pantalla('* Respuesta *', 0, 20)
    mi_robot.escribe_pantalla('* Correcta! *', 0, 30)
    mi_robot.escribe_pantalla('*           *', 0, 40)
    mi_robot.escribe_pantalla('*************', 0, 50)
    time.sleep(3)
    

def mostrar_menu_incorrecto():
    mi_robot.borra_pantalla()
    mi_robot.escribe_pantalla('*************', 0, 0)
    mi_robot.escribe_pantalla('*           *', 0, 10)
    mi_robot.escribe_pantalla('* Respuesta *', 0, 20)
    mi_robot.escribe_pantalla('*Incorrecta!*', 0, 30)
    mi_robot.escribe_pantalla('*           *', 0, 40)
    mi_robot.escribe_pantalla('*************', 0, 50)
    time.sleep(3)
    
def mostrar_menu_final(puntuacion):
    mi_robot.borra_pantalla()
    resultado = f'*    {puntuacion}      *'
    mi_robot.escribe_pantalla('*************', 0, 0)
    mi_robot.escribe_pantalla('*           *', 0, 10)
    mi_robot.escribe_pantalla('*Tus puntos:*', 0, 20)
    mi_robot.escribe_pantalla(str(resultado), 0, 30)
    mi_robot.escribe_pantalla('*           *', 0, 40)
    mi_robot.escribe_pantalla('*************', 0, 50)
    time.sleep(3)
            
def main():
    seleccion_jugador = mostrar_menu_inicial()
    if seleccion_jugador == 'salir':
        mostrar_menu_salida()
        mi_robot.borra_pantalla()
    elif seleccion_jugador == 'jugar':
        mostrar_menu_aviso_estructura()
        mostrar_menu_estructura()
        puntuacion = mostrar_menu_jugar()
        mi_robot.borra_pantalla()
        mostrar_menu_final(puntuacion)
    elif seleccion_jugador == 'error':
        return 'cierre por error'

if __name__ == '__main__':
    main()

