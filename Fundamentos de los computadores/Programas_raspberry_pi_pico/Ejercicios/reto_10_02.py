from complubot.libreria_dodo import dodo
from machine import *
import time

boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN) 
led_rgb = dodo()
tiempo_apagado = 0.2

def apagado():
    led_rgb.apaga_rgb(0)
    led_rgb.apaga_rgb(1)
    led_rgb.apaga_rgb(2)
    led_rgb.apaga_rgb(3)
    led_rgb.apaga_rgb(4)

def comprobacion_corte_programa():
    if boton_derecha.value() == 1:
        apagado()
        sys.exit()

def coche_fantastico():
    while boton_derecha.value() != 1:
        # ENCENDIDO DEL PRIMER LED
        led_rgb.enciende_rgb(0, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL SEGUNDO LED Y APAGADO DEL PRIMERO
        led_rgb.apaga_rgb(0)
        led_rgb.enciende_rgb(1, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL TERCER LED Y APAGADO DEL SEGUNDO
        led_rgb.apaga_rgb(1)
        led_rgb.enciende_rgb(2, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL CUARTO LED Y APAGADO DEL TERCERO
        led_rgb.apaga_rgb(2)
        led_rgb.enciende_rgb(3, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL QUINTO LED Y APAGADO DEL CUARTO
        led_rgb.apaga_rgb(3)
        led_rgb.enciende_rgb(4, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL CUARTO LED Y APAGADO DEL QUINTO
        led_rgb.apaga_rgb(4)
        led_rgb.enciende_rgb(3, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL TERCER LED Y APAGADO DEL CUARTO 
        led_rgb.apaga_rgb(3)
        led_rgb.enciende_rgb(2, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL SEGUNDO LED Y APAGADO DEL TERCER
        led_rgb.apaga_rgb(2)
        led_rgb.enciende_rgb(1, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # ENCENDIDO DEL PRIMER LED Y APAGADO DEL SEGUNDO
        led_rgb.apaga_rgb(1)
        led_rgb.enciende_rgb(0, led_rgb.rojo)
        time.sleep(tiempo_apagado)
        comprobacion_corte_programa()
        # APAGADO DEL PRIMER LED
        led_rgb.apaga_rgb(0)
        comprobacion_corte_programa()

def main():
    apagado()
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            coche_fantastico()

main()        
