from complubot.libreria_dodo import dodo
from machine import *
import time

boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN) 
mi_robot = dodo()

def apagado():
    mi_robot.apaga_rgb(0)
    mi_robot.apaga_rgb(1)
    mi_robot.apaga_rgb(2)
    mi_robot.apaga_rgb(3)
    mi_robot.apaga_rgb(4)

# PROGRAMA SEMAFORO FORMULA 1
while True:
    apagado()
    if boton_izquierda.value() == 1:
        mi_robot.enciende_rgb(0,mi_robot.rojo)
        time.sleep(1)
        mi_robot.enciende_rgb(1,mi_robot.rojo)
        time.sleep(1)
        mi_robot.enciende_rgb(2,mi_robot.rojo)
        time.sleep(1)
        mi_robot.enciende_rgb(3,mi_robot.rojo)
        time.sleep(1)
        mi_robot.enciende_rgb(4,mi_robot.rojo)
        while boton_derecha.value() != 1:
            time.sleep(0.5)
        apagado()

        
