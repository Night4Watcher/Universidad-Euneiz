from complubot.libreria_dodo import dodo
import time

led_rgb = dodo()

# Color A (inicio): azul
color_a = (0, 0, 255)

# Color B (fin): rojo
color_b = (255, 0, 0)

# Cantidad de LEDs (en dodo: 5 LEDs RGB)
num_leds = 5

# Apagar todos antes de empezar
for i in range(num_leds):
    led_rgb.apaga_rgb(i)

def calcular_color_intermedio(color1, color2, paso, total_pasos):
    r = int(color1[0] + (color2[0] - color1[0]) * paso / (total_pasos - 1))
    g = int(color1[1] + (color2[1] - color1[1]) * paso / (total_pasos - 1))
    b = int(color1[2] + (color2[2] - color1[2]) * paso / (total_pasos - 1))
    return (r, g, b)

# Aplicar degradado
for i in range(num_leds):
    color = calcular_color_intermedio(color_a, color_b, i, num_leds)
    led_rgb.enciende_rgb(i, color)

# Mantener encendido un rato
time.sleep(10)

# Apagar todos
for i in range(num_leds):
    led_rgb.apaga_rgb(i)
