import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

boton1 = tk.Button(ventana, text= "Boton 1")
boton1.pack(side=tk.TOP, fill=tk.X)

boton2 = tk.Button(ventana, text= "Boton 2")
boton2.pack(side=tk.BOTTOM, fill=tk.X)

boton3 = tk.Button(ventana, text= "Boton 3")
boton3.pack(side=tk.LEFT, fill=tk.Y)

boton4 = tk.Button(ventana, text= "Boton 4")
boton4.pack(side=tk.RIGHT, fill=tk.Y)

ventana.mainloop()