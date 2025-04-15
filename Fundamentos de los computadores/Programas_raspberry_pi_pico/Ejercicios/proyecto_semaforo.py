# PROYECTO SEMAFORO

from machine import *
from complubot.libreria_dodo import dodo
import time

# DEFINIMOS LAS VARIABLES QUE UTILIZAREMOS EN EL PROGRAMA
boton_izquierda = Pin(20, Pin.IN) 
boton_derecha = Pin(21, Pin.IN)
led_rojo_coches = Pin(17, Pin.OUT)
led_amarillo_coches = Pin(18, Pin.OUT)
led_verde_coches = Pin(19, Pin.OUT)
led_rojo_peatones = Pin(15, Pin.OUT)
led_verde_peatones = Pin(16, Pin.OUT)
zumbador = PWM(14)

def apagado():
    led_rojo_coches.off()
    led_amarillo_coches.off()
    led_verde_coches.off()
    led_rojo_peatones.off()
    led_verde_peatones.off()
    zumbador.duty_u16(0)

def estado_inicial():
    # ESTADO DEL SEMAFORO DE PEATONES
    led_rojo_peatones.on()
    led_verde_peatones.off()
    # ESTADO DEL SEMAFORO DE COCHES
    led_verde_coches.on()
    led_amarillo_coches.off()
    led_rojo_coches.off()
    # ESTADO DEL ZUMBADOR
    zumbador.duty_u16(0)
    
def secuencia_activacion():
    time.sleep(5)
    semaforo_vehiculos_ambar()
    time.sleep(5)
    semaforo_vehiculos_rojo()
    time.sleep(2)
    semaforo_peatones_verde()
    time.sleep(5)
    # SECUENCIA DE PARPADEO DEL SEMAFORO DE PEATONES
    for parpadeos in range(5):
        zumbador.duty_u16(0)
        led_verde_peatones.off()
        time.sleep(1)
        zumbador.duty_u16(30000)
        zumbador.freq(125)
        led_verde_peatones.on()
        time.sleep(1)
    zumbador.duty_u16(0)
    semaforo_peatones_rojo()
    time.sleep(5)
    semaforo_vehiculos_verde()

# FUNCION QUE PONE EL SEMAFORO DE VEHICULOS EN VERDE
def semaforo_vehiculos_verde():
    led_verde_coches.on()
    led_amarillo_coches.off()
    led_rojo_coches.off()
    
# FUNCION QUE PONE EL SEMAFORO DE VEHICULOS EN AMBAR
def semaforo_vehiculos_ambar():
    led_verde_coches.off()
    led_amarillo_coches.on()
    led_rojo_coches.off()
    
# FUNCION QUE PONE EL SEMAFORO DE VEHICULOS EN ROJO
def semaforo_vehiculos_rojo():
    led_verde_coches.off()
    led_amarillo_coches.off()
    led_rojo_coches.on()

# FUNCION QUE PONE EL SEMAFORO DE PEATONES EN VERDE
def semaforo_peatones_verde():
    led_verde_peatones.on()
    led_rojo_peatones.off()

# FUNCION QUE PONE EL SEMAFORO DE PEATONES EN ROJO
def semaforo_peatones_rojo():
    led_verde_peatones.off()
    led_rojo_peatones.on()
    
# FUNCION PRINCIPAL DEL PROGRAMA
def main():
    while boton_derecha.value() != 1:
        estado_inicial()
        if boton_izquierda.value() == 1:
            secuencia_activacion()
    apagado()
    
main()