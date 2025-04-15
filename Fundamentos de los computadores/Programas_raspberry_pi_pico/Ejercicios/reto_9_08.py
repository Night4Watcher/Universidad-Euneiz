# RETO 9_08

from machine import *
from complubot.libreria_dodo import dodo
import time

# DEFINIMOS LAS VARIABLES QUE UTILIZAREMOS EN EL PROGRAMA
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)
led_rojo = Pin(10, Pin.OUT)
led_amarillo = Pin(11, Pin.OUT)
led_blanco = Pin(13, Pin.OUT)

def apagado():
    led_rojo.off()
    led_blanco.off()
    
def parpadeo_inverso():
    while boton_derecha.value() != 1:
        # SECUENCIA CON EL LED ROJO ENCENDIDO
        led_rojo.on()
        led_blanco.off()
        time.sleep(1)
        # SECUENCIA CON EL LED BLANCO ENCENDIDO
        led_rojo.off()
        led_blanco.on()
        time.sleep(1)
        
def main():
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            parpadeo_inverso()
        apagado()
    
main()