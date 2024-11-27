import tkinter as tk
import os

def saludar():
    etiqueta.config(text="¡Hola, GILIPOLLAS!")
    
def despedida():
    etiqueta.config(text="Adios, SUBNORMAL")
    
root = tk.Tk()
root.title("Saludo cariñoso")

# Tamaño de la ventana
root.geometry("400x300") # Se le puede introducir un offset (tamaño) + (offset)

# Texto en la pantalla
etiqueta = tk.Label(root, text="PULSA EL BOTON!")
etiqueta.pack()  # pack() agrega y organiza el widget en la ventana

# Botones funcionales
boton = tk.Button(root, text="PULSAME!!!", command=saludar)
boton.pack()

boton_2 = tk.Button(root, text="No me pulses", command=despedida)
boton_2.pack()

root.mainloop()
