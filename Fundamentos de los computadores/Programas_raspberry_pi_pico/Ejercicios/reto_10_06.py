from complubot.libreria_dodo import dodo
from machine import *
import random
import time

boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN) 
led_rgb = dodo()
tiempo_apagado = random.randint(1, 3)

def apagado():
    led_rgb.apaga_rgb(0)
    led_rgb.apaga_rgb(1)
    led_rgb.apaga_rgb(2)
    led_rgb.apaga_rgb(3)
    led_rgb.apaga_rgb(4)
    
def semaforo():
    led_rgb.enciende_rgb(0, led_rgb.rojo)
    time.sleep(1)
    led_rgb.enciende_rgb(1, led_rgb.rojo)
    time.sleep(1)
    led_rgb.enciende_rgb(2, led_rgb.rojo)
    time.sleep(1)
    led_rgb.enciende_rgb(3, led_rgb.rojo)
    time.sleep(1)
    led_rgb.enciende_rgb(4, led_rgb.rojo)
    time.sleep(tiempo_apagado)

def main():
    while boton_derecha.value() != 1:
        apagado()
        if boton_izquierda.value() == 1:
            semaforo()
    
main()
