# RETO 9_04

from machine import *
from complubot.libreria_dodo import dodo
import time

# DEFINIMOS LAS VARIABLES QUE UTILIZAREMOS EN EL PROGRAMA
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)
led_placa_3 = Pin(3, Pin.OUT)
led_placa_22 = Pin(22, Pin.OUT)

def apagado():
    led_placa_3.off()
    led_placa_22.off()
    
def encendido_led():
    led_placa_3.on()
    led_placa_22.on()
    time.sleep(5)
    
def main():
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            encendido_led()
        apagado()
        
main()