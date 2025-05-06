from complubot.libreria_dodo import dodo
from machine import *
import time

boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN) 
led_rgb = dodo()
tiempo_apagado = 1

def apagado():
    led_rgb.apaga_rgb(0)
    led_rgb.apaga_rgb(1)
    led_rgb.apaga_rgb(2)
    led_rgb.apaga_rgb(3)
    led_rgb.apaga_rgb(4)
    

def alarma():
    for parpadeos in range(5):
        # ENCENDIDO DE TODOS LOS LEDS
        for led in range(5):
            led_rgb.enciende_rgb(led, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        # APAGADO DE TODOS LOS LEDS
        for led in range(5):
            led_rgb.apaga_rgb(led)
        time.sleep(tiempo_apagado)

def main():
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            alarma()

main()
