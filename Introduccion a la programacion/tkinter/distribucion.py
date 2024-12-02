import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x200")

# CREACION DE LA CUADRICULA DE REFERENCIA
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

# BOTONES CON DIFERENTES VALORES DE STICKY
boton_1 = tk.Button(ventana, text="Norte")
boton_1.grid(row=0, column=0, sticky="nsew")

boton_2 = tk.Button(ventana, text="Boton 2")
boton_2.grid(row=0, column= 1, sticky="nsew")

boton_3 = tk.Button(ventana, text="Norte")
boton_3.grid(row=1, column=0, sticky="nsew")

boton_4 = tk.Button(ventana, text="Boton 2")
boton_4.grid(row=1, column= 1, sticky="nsew")

ventana.mainloop()