import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")

# CREACION DE LA CUADRICULA DE REFERENCIA
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

# DISTRIBUCION DE LOS BOTONES
boton = tk.Button(ventana, text="Arriba")
boton.grid(row=0, column=0, sticky="n")

boton2 = tk.Button(ventana, text="Abajo")
boton2.grid(row=0, column=0, sticky="s")

boton3 = tk.Button(ventana, text="Izquiera")
boton3.grid(row=0, column=0, sticky="w")

boton4 = tk.Button(ventana, text="Derecha")
boton4.grid(row=0, column=0, sticky="e")

# DISTRIBUCION DE LOS BOTONES
boton5 = tk.Button(ventana, text="Arriba")
boton5.grid(row=0, column=1, sticky="n")

boton6 = tk.Button(ventana, text="Abajo")
boton6.grid(row=0, column=1, sticky="s")

boton7 = tk.Button(ventana, text="Izquiera")
boton7.grid(row=0, column=1, sticky="w")

boton8 = tk.Button(ventana, text="Derecha")
boton8.grid(row=0, column=1, sticky="e")

# DISTRIBUCION DE LOS BOTONES
boton9 = tk.Button(ventana, text="Arriba")
boton9.grid(row=1, column=0, sticky="n")

boton10 = tk.Button(ventana, text="Abajo")
boton10.grid(row=1, column=0, sticky="s")

boton11 = tk.Button(ventana, text="Izquiera")
boton11.grid(row=1, column=0, sticky="w")

boton12 = tk.Button(ventana, text="Derecha")
boton12.grid(row=1, column=0, sticky="e")

# DISTRIBUCION DE LOS BOTONES
boton13 = tk.Button(ventana, text="Arriba")
boton13.grid(row=1, column=1, sticky="n")

boton13 = tk.Button(ventana, text="Abajo")
boton13.grid(row=1, column=1, sticky="s")

boton14 = tk.Button(ventana, text="Izquiera")
boton14.grid(row=1, column=1, sticky="w")

boton15 = tk.Button(ventana, text="Derecha")
boton15.grid(row=1, column=1, sticky="e")

ventana.mainloop()