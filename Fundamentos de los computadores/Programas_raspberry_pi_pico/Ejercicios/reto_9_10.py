# RETO 9_10

from machine import *
from complubot.libreria_dodo import dodo
import time

# DEFINIMOS LAS VARIABLES QUE UTILIZAREMOS EN EL PROGRAMA
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)
led_rojo = Pin(10, Pin.OUT)
led_amarillo = Pin(11, Pin.OUT)
led_verde = Pin(12, Pin.OUT)
led_blanco = Pin(13, Pin.OUT)

def apagado():
    led_rojo.off()
    led_amarillo.off()
    led_verde.off()
    led_blanco.off()
    
def efecto_escalera():
    while boton_derecha.value() != 1:
        ascendente()
        time.sleep(0.5)
        descendente()
        time.sleep(0.5)

def ascendente():
    # SECUENCIA CON LED ROJO ENCENDIDO
    led_rojo.on()
    led_amarillo.off()
    led_verde.off()
    led_blanco.off()
    time.sleep(0.5)
    # SECUENCIA CON LED AMARILLO ENCENDIDO
    led_rojo.off()
    led_amarillo.on()
    led_verde.off()
    led_blanco.off()
    time.sleep(0.5)
    # SECUENCIA CON LED VERDE ENCENDIDO
    led_rojo.off()
    led_amarillo.off()
    led_verde.on()
    led_blanco.off()
    time.sleep(0.5)
    # SECUENCIA CON LED BLANCO ENCENDIDO
    led_rojo.off()
    led_amarillo.off()
    led_verde.off()
    led_blanco.on()
    time.sleep(0.5)

def descendente():
    # SECUENCIA CON EL LED VERDE ENCENDIDO
    led_rojo.off()
    led_amarillo.off()
    led_verde.on()
    led_blanco.off()
    time.sleep(0.5)
    # SECUENCIA CON EL LED AMARILLO ENCENDIDO
    led_rojo.off()
    led_amarillo.on()
    led_verde.off()
    led_blanco.off()
    time.sleep(0.5)
    # SECUENCIA CON EL LED ROJO ENCENDIDO
    led_rojo.on()
    led_amarillo.off()
    led_verde.off()
    led_blanco.off()
    time.sleep(0.5)

def main():
    while boton_derecha.value() != 1:
        if boton_izquierda.value() == 1:
            efecto_escalera()
        apagado()
    
main()