# RETO 9_06

from machine import *
from complubot.libreria_dodo import dodo
import time

# DEFINIMOS LAS VARIABLES QUE UTILIZAREMOS EN EL PROGRAMA
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)
led_rojo = Pin(10, Pin.OUT)

def apagado():
    led_rojo.off()

def encendido_intermitente():
    while boton_derecha.value() != 1:
        led_rojo.on()
        time.sleep(0.5)
        led_rojo.off()
        time.sleep(0.5)

def main():
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            encendido_intermitente()
        apagado()

main()