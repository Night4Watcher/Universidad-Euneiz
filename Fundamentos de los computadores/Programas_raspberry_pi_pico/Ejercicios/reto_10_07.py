from complubot.libreria_dodo import dodo
from machine import *
import random
import time

boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN) 
led_rgb = dodo()
tiempo_apagado = 0.2
zumbador = PWM(Pin(14))

def apagado():
    led_rgb.apaga_rgb(0)
    led_rgb.apaga_rgb(1)
    led_rgb.apaga_rgb(2)
    led_rgb.apaga_rgb(3)
    led_rgb.apaga_rgb(4)
    zumbador.duty_u16(0)
    
def coche_policia():
    zumbador.duty_u16(30000)
    while boton_derecha.value() != 1:
        izquierda = [0, 1]
        derecha = [3, 4]
        led_rgb.enciende_rgb(2, led_rgb.blanco)
        for _ in izquierda:
            led_rgb.enciende_rgb(_, led_rgb.azul)
        for _ in derecha:
            led_rgb.apaga_rgb(_)
        zumbador.freq(1000)
        time.sleep(tiempo_apagado)
        for _ in derecha:
            led_rgb.enciende_rgb(_, led_rgb.rojo)
        for _ in izquierda:
            led_rgb.apaga_rgb(_)
        zumbador.freq(500)
        time.sleep(tiempo_apagado)

def main():
    while boton_derecha.value() != 1:
        apagado()
        if boton_izquierda.value() == 1:
            coche_policia()
    apagado()

main()
