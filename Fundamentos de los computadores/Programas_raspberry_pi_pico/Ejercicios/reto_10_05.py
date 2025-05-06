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

def estado_inicial():
    led_rgb.enciende_rgb(0, led_rgb.verde)
    secuencia = [1,2,4]
    for led in secuencia:
        led_rgb.apaga_rgb(led)
    led_rgb.enciende_rgb(3, led_rgb.rojo)

def semaforo_activado():
    # ALTERNAR SEMAFORO DE COCHES A AMARILLO
    led_rgb.apaga_rgb(0)
    led_rgb.enciende_rgb(1, led_rgb.amarillo)
    time.sleep(3)
    # ALTERNAR SEMAFORO DE PEATONES A VERDE Y COCHES A ROJO
    led_rgb.apaga_rgb(1)
    led_rgb.enciende_rgb(2, led_rgb.rojo)
    led_rgb.apaga_rgb(3)
    led_rgb.enciende_rgb(4, led_rgb.verde)
    time.sleep(3)

def main():
    while boton_derecha.value() != 1:
        estado_inicial()
        if boton_izquierda.value() == 1:
            semaforo_activado()
    apagado()

main()
